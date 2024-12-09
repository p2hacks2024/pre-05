import json
import os
import requests
from dotenv import load_dotenv
from requests.exceptions import RequestException

# .envファイルを読み込む
load_dotenv()

# Google Search APIのエンドポイントとAPIキー
GOOGLE_SEARCH_API_URL = "https://www.googleapis.com/customsearch/v1"
API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
CX = "24692ceba26ed4121"  # カスタム検索エンジンID

def get_search_count(query):
    params = {
        'key': API_KEY,
        'cx': CX,
        'q': query
    }
    try:
        response = requests.get(GOOGLE_SEARCH_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get('searchInformation', {}).get('totalResults', 0)
    except RequestException as e:
        print(f"Error fetching search count for {query}: {e}")
        return 0

# tokyo_restaurants.jsonを読み込む
with open('tokyo_restaurants.json', 'r', encoding='utf-8') as file:
    restaurants = json.load(file)

# 検索結果を格納するリスト
search_results = []

# 各飲食店名でグーグル検索された回数を取得してリストに追加
total = len(restaurants)
for i, restaurant in enumerate(restaurants, 1):
    name = restaurant['name']
    print(f"Processing {i}/{total}: {name}")
    search_count = get_search_count(name)
    search_results.append({'name': name, 'search_count': search_count})


# 結果をtokyo_SearchCount.jsonに書き込む
with open('tokyo_SearchCount.json', 'w', encoding='utf-8') as file:
    json.dump(search_results, file, ensure_ascii=False, indent=4)

print("検索結果をtokyo_SearchCount.jsonに出力しました。")