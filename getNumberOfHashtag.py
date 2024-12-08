import requests
from dotenv import load_dotenv
import os

# .env ファイルから環境変数を読み取る
load_dotenv()

# 環境変数から必要な情報を取得
ACCESS_TOKEN = os.getenv("INSTAGRAM_API_TOKEN")  # Instagram API トークン
USER_ID = os.getenv("INSTAGRAM_USER_ID")  # Instagram ユーザー ID
BASE_URL = "https://graph.facebook.com/v21.0"  # Instagram Graph API のベース URL

# 1. ハッシュタグIDを取得する
def get_hashtag_id(hashtag):
    url = f"{BASE_URL}/ig_hashtag_search?user_id={USER_ID}&q={hashtag}&access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()
    
    if "data" in data and len(data["data"]) > 0:
        return data["data"][0]["id"]  # 最初のハッシュタグIDを返す
    else:
        print("Error: ハッシュタグIDが見つかりません")
        print(f"Response: {data}")
        return None

# 2. ハッシュタグの投稿数を取得する（ページング対応）
def get_hashtag_post_count(hashtag_id):
    url = f"{BASE_URL}/{hashtag_id}/recent_media?user_id={USER_ID}&fields=id,caption&access_token={ACCESS_TOKEN}"
    total_count = 0
    while url:
        response = requests.get(url)
        data = response.json()
        
        if "data" in data:
            total_count += len(data["data"])  # 現在のページの投稿数をカウント
            # 次のページがある場合、'paging'キーの 'next' を使って次のURLを取得
            url = data.get("paging", {}).get("next")
        else:
            print("Error: 投稿が見つかりません")
            print(f"Response: {data}")
            break
            
    return total_count

# メイン処理
if __name__ == "__main__":
    hashtag = "函館山"  # 調べたいハッシュタグ
    hashtag_id = get_hashtag_id(hashtag)
    
    if hashtag_id:
        post_count = get_hashtag_post_count(hashtag_id)
        print(f"ハッシュタグ #{hashtag} の投稿数: {post_count}")
