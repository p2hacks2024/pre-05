import json
import os
import django

# Djangoプロジェクトの設定を読み込む
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'experiment_project.settings')
django.setup()

from myapp.models import HakodateRestaurant

def import_restaurants():
    with open('03hakodate_restaurants_converted.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            HakodateRestaurant.objects.create(
                name=item['店舗名'],
                address=item['住所'],
                latitude=item['緯度'],
                longitude=item['経度'],
                review_count=item.get('レビュー数', 0),
                restaurant_id=item['shopid'],
                url_pc=item['url']['pc'],
                logo_image=item.get('ロゴ画像', 'https://imgfp.hotp.jp/IMGH/70/08/P033307008/P033307008_69.jpg')
            )

if __name__ == '__main__': 
    import_restaurants()