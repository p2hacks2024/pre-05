import json
import os
import django

# Djangoプロジェクトの設定を読み込む
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'experiment_project.settings')
django.setup()

from myapp.models import HakodateRestaurant

def truncate_text(text, max_length=1000):
    """テキストを指定された長さに制限する"""
    if text and len(text) > max_length:
        return text[:max_length-3] + "..."
    return text

def import_reviews():
    try:
        print(f"現在の作業ディレクトリ: {os.getcwd()}")
        
        input_file = 'place_details_converted.json'  # 変換後のファイルを使用
        
        if not os.path.exists(input_file):
            print(f"エラー: {input_file} が見つかりません")
            return

        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f"読み込んだデータ数: {len(data)}")
            
            for item in data:
                try:
                    restaurant = HakodateRestaurant.objects.filter(name=item.get('店舗名')).first()
                    if restaurant:
                        print("-" * 50)
                        print(f"店舗名: {item.get('店舗名')}")
                        
                        # レビュー数の処理
                        review_count = item.get('レビュー数', 0)
                        restaurant.review_count = int(review_count) if isinstance(review_count, int) else 0
                        
                        # レビューの処理（キー名を修正）
                        review = item.get('ピックアップレビュー', '')  # キーを'ピックアップレビュー'に変更
                        review = truncate_text(review, 1000)
                        
                        print(f"取得したレビュー: {review}")  # デバッグ出力を追加
                        restaurant.pickup_review = review
                        restaurant.save()
                        print(f"保存完了 - 店舗: {restaurant.name}")
                        print(f"保存したレビュー: {restaurant.pickup_review}")  # 保存後の確認
                except Exception as e:
                    print(f"店舗処理中にエラー: {str(e)}")
                    continue
                    
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")

if __name__ == '__main__':
    print("スクリプト開始")
    import_reviews()
    print("スクリプト終了")