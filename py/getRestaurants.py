import requests
import json
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# APIキーを環境変数から取得
API_KEY = os.getenv('HOT_PEPPER_API_KEY')

# リクエストURL
URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

# 検索条件を設定する関数
def get_data(keywords, count=None):
    # 複数のキーワードをスペースで区切って結合
    keyword_str = ' '.join(keywords)
    
    # 検索条件を設定
    params = {
        'key': API_KEY,
        'keyword': keyword_str,
        'format': 'json',
        'count': count if count else 1000,  # 指定された件数か最大100件を取得
        'start': 1
    }
    
    results = []
    print(f"検索キーワード: {keyword_str}")
    while True:
        print(f"リクエスト送信中... (開始位置: {params['start']})")
        # APIリクエストを送信
        response = requests.get(URL, params=params)
        datum = response.json()

        if response.status_code != 200:
            print(f"HTTPエラー: {response.status_code}")
            break
        
        # データが取得できない場合は終了
        if 'results' not in datum or 'shop' not in datum['results']:
            print("検索に失敗しました。")
            break
        
        print(f"取得したデータ件数: {len(datum['results']['shop'])}件")
        # 取得したデータをリストに追加
        stores = datum['results']['shop']
        results.extend([{
            '店舗名': store.get('name', 'N/A'),
            '緯度': store.get('lat', 'N/A'),
            '経度': store.get('lng', 'N/A'),
            '住所': store.get('address', 'N/A'),
            'shopid': store.get('id', 'N/A'),
            'url': store.get('urls', 'N/A'),
            'ロゴ画像': store.get('logo_image', 'N/A'),
        } for store in stores])

        # 全て取得する場合
        if not count:
            if len(results) >= datum['results']['results_available']:
                break
            params['start'] += 100  # 次の100件を取得するために開始位置を更新
        else:
            break

    return results

# データをJSONに保存する関数
def save_to_json(results, filename='hakodate_restaurants.json'):
    try:
        if results:
            output_directory = 'js'  # ディレクトリを修正
            os.makedirs(output_directory, exist_ok=True)  # ディレクトリが存在しない場合は作成
            output_file_path = os.path.join(output_directory, filename)
            with open(output_file_path, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"JSONファイル '{output_file_path}' に保存されました！")
        else:
            print("保存するデータがありません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

# メイン処理
if __name__ == "__main__":
    # 検索キーワードをターミナルから入力
    keywords = input("検索キーワードをスペースで区切って入力してください（例: 'カフェ 江別市 パン屋さん'）: ").split()
    
    # データ取得方法を選択
    print("データ取得方法を選んでください:")
    print("1: すべて抽出する")
    print("2: 指定件数を抽出する")
    choice = input("選択 (1 または 2): ")

    if choice == '1':
        count = None  # 全てを取得
    elif choice == '2':
        count = int(input("抽出する件数を入力してください: "))
    else:
        print("無効な選択です。プログラムを終了します。")
        exit()

    # データ取得とJSON保存
    results = get_data(keywords, count)
    save_to_json(results)
