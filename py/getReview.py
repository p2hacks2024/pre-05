import requests
import json
from dotenv import load_dotenv
import os
import re

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
            'fields': 'rating,user_ratings_total,reviews',  # reviewsを追加
            'key': API_KEY
        }

        # 場所の詳細リクエスト
        response = requests.get(details_url, params=details_params)
        details = response.json()
        
        # 総レビュー数を取得
        review_count = details.get('result', {}).get('user_ratings_total', 0)
        
        # 日本語のレビューをフィルタリング
        reviews = details.get('result', {}).get('reviews', [])
        japanese_reviews = [review for review in reviews if re.search(r'[ぁ-んァ-ン一-龥]', review['text'])]
        
        # 日本語のレビューがない場合は英語のレビューを使用
        picked_review = japanese_reviews[0]['text'] if japanese_reviews else (reviews[0]['text'] if reviews else "レビューが見つかりませんでした。")
        
        return review_count, picked_review
    
    return 0, "レビューが見つかりませんでした。"

def main():
    # hakodate_restaurants.jsonを読み込む
    with open(r'C:\VScode\TrendFlash2\pre-05\js\hakodate_restaurants.json', 'r', encoding='utf-8') as f:
        restaurants = json.load(f)

    results = []
    
    for i, restaurant in enumerate(restaurants):
        print(f"処理中... {i+1}/{len(restaurants)}: {restaurant['店舗名']}")
        
        review_count, picked_review = get_place_reviews(restaurant['店舗名'])
        results.append({
            "店舗名": restaurant['店舗名'],
            "レビュー数": review_count,
            "ピックアップレビュー": picked_review
        })

    # 結果をJSONファイルに保存
    with open(r'C:\VScode\TrendFlash2\pre-05\js\place_details.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("処理が完了しました。データはplace_details.jsonに保存されました。")

if __name__ == "__main__":
    main()