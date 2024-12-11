import requests
import json
from dotenv import load_dotenv
import os
import time

# .envファイルの読み込み
load_dotenv()

# .envファイルからAPIキーを取得
API_KEY = os.getenv('GOOGLE_MAP_API_KEY')

def get_place_reviews(shop_name):
    # 場所の検索エンドポイント
    search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    search_params = {
        'input': shop_name,
        'inputtype': 'textquery',
        'fields': 'place_id',
        'key': API_KEY
    }

    # 場所の検索リクエスト
    response = requests.get(search_url, params=search_params)
    response_data = response.json()

    if 'candidates' in response_data and len(response_data['candidates']) > 0:
        place_id = response_data['candidates'][0]['place_id']
        
        # 場所の詳細エンドポイント
        details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        details_params = {
            'place_id': place_id,
            'fields': 'rating,user_ratings_total',  # reviews_countの代わりにuser_ratings_totalを使用
            'key': API_KEY
        }

        # 場所の詳細リクエスト
        response = requests.get(details_url, params=details_params)
        details = response.json()
        
        # 総レビュー数を取得
        return details.get('result', {}).get('user_ratings_total', 0)
    
    return 0

def main():
    # hakodate_restaurants.jsonを読み込む
    with open('hakodate_restaurants.json', 'r', encoding='utf-8') as f:
        restaurants = json.load(f)

    results = []
    
    for i, restaurant in enumerate(restaurants):
        print(f"処理中... {i+1}/{len(restaurants)}: {restaurant['店舗名']}")
        
        # Google Places APIの制限を考慮してスリープを入れる
        # time.sleep(2)
        
        review_count = get_place_reviews(restaurant['店舗名'])
        results.append({
            "店舗名": restaurant['店舗名'],
            "レビュー数": review_count
        })

    # 結果をJSONファイルに保存
    with open('place_details.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("処理が完了しました。データはplace_details.jsonに保存されました。")

if __name__ == "__main__":
    main()