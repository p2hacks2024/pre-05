import json
import os
import requests
import re
from dotenv import load_dotenv
from requests.exceptions import RequestException

# .envファイルを読み込む
load_dotenv()

# Google Search APIの設定
GOOGLE_SEARCH_API_URL = "https://www.googleapis.com/customsearch/v1"
API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
CX = "24692ceba26ed4121"

# 除外する一般的な用語
GENERIC_TERMS = {
    'バー', 'カフェ', 'レストラン', '食堂', '居酒屋', '焼肉',
    '酒場', 'キッチン', '亭', '軒', '函館', '北海道', '大門',
    'bar', 'cafe', '店', '屋', '処', 'ホテル', '駅前'
}

def clean_restaurant_name(name):
    """店名のクリーニング処理"""
    # 地域特有の表記を削除
    name = name.replace('函館駅前店', '').replace('函館店', '')
    
    # カタカナ、ひらがな、漢字を優先的に抽出
    japanese_chars = re.findall(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]+', name)
    if japanese_chars:
        cleaned_name = ' '.join(japanese_chars)
    else:
        # 日本語文字がない場合は元の名前から一般的な用語を除去
        name_parts = name.split()
        specific_parts = [part for part in name_parts if part.upper() not in [term.upper() for term in GENERIC_TERMS]]
        cleaned_name = ' '.join(specific_parts) if specific_parts else name
    
    return cleaned_name.strip()

def get_search_count_with_retry(query, max_retries=3):
    """検索回数取得（リトライ機能付き）"""
    for attempt in range(max_retries):
        try:
            cleaned_query = clean_restaurant_name(query)
            search_query = f'({query} OR "{cleaned_query}") (函館 OR 北海道) (店舗 OR レストラン OR グルメ)'
            
            params = {
                'key': API_KEY,
                'cx': CX,
                'q': search_query,
                'gl': 'jp',
                'lr': 'lang_ja',
                'dateRestrict': 'y1'
            }
            
            response = requests.get(GOOGLE_SEARCH_API_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            count = int(data.get('searchInformation', {}).get('totalResults', 0))
            
            if count > 0:
                return count
            
        except Exception as e:
            print(f"Attempt {attempt + 1} failed for {query}: {e}")
            if attempt < max_retries - 1:
                continue
    
    return 0

def main():
    """メイン処理"""
    # 飲食店データの読み込み
    with open('hakodate_restaurants.json', 'r', encoding='utf-8') as file:
        restaurants = json.load(file)

    # 検索結果を格納するリスト
    search_results = []
    total = len(restaurants)

    # 各店舗の検索回数を取得
    for i, restaurant in enumerate(restaurants, 1):
        name = restaurant['name']
        print(f"Processing {i}/{total}: {name}")
        
        search_count = get_search_count_with_retry(name)
        result = {
            'name': name,
            'search_count': str(search_count),
            'cleaned_name': clean_restaurant_name(name)
        }
        search_results.append(result)
    

    # 結果をJSONファイルに保存
    with open('hakodate_SearchCount.json', 'w', encoding='utf-8') as file:
        json.dump(search_results, file, ensure_ascii=False, indent=4)

    print("検索結果をhakodate_SearchCount.jsonに出力しました。")

if __name__ == "__main__":
    main()