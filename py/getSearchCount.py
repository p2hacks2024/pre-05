import json
import requests
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# Google Custom Search APIの設定
API_KEY = os.getenv('GOOGLE_SEARCH_API_KEY')
SEARCH_ENGINE_ID = 'YOUR_SEARCH_ENGINE_ID'  # ここに検索エンジンIDを入力してください

# 飲食店の検索回数を取得する関数
def get_search_count(restaurant_name):
    search_url = f"https://www.googleapis.com/customsearch/v1?q={restaurant_name}&key={API_KEY}&cx={SEARCH_ENGINE_ID}"
    response = requests.get(search_url)
    data = response.json()
    
    # 検索結果の件数を取得
    if 'searchInformation' in data:
        count = int(data['searchInformation']['totalResults'])
    else:
        count = 0
    
    return count

# メイン処理
def main():
    # スクリプトのディレクトリを取得
    script_dir = os.path.dirname(__file__)
    
    # 飲食店データの読み込み
    json_path = os.path.join(script_dir, 'hakodate_restaurants.json')
    with open(json_path, 'r', encoding='utf-8') as file:
        restaurants = json.load(file)

    # 検索結果を格納するリスト
    search_results = []
    total = len(restaurants)

    # 各店舗の検索回数を取得
    for i, restaurant in enumerate(restaurants, 1):
        name = restaurant['店舗名']
        print(f"Processing {i}/{total}: {name}")
        
        search_count = get_search_count(name)
        result = {
            'name': name,
            'search_count': search_count
        }
        search_results.append(result)

    # 結果をJSONファイルに保存
    output_path = os.path.join(script_dir, 'SearchCount.json')
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(search_results, file, ensure_ascii=False, indent=4)

    print("検索結果をSearchCount.jsonに出力しました。")

if __name__ == "__main__":
    main()