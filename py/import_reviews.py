import json
import os
import django

# Djangoプロジェクトの設定を読み込む
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'experiment_project.settings')
django.setup()

from myapp.models import HakodateRestaurant

def import_reviews():
    with open('place_details.json', 'r', encoding='utf-8') as file:  # ファイルパスを確認
        data = json.load(file)
        for item in data:
            restaurant = HakodateRestaurant.objects.filter(name=item.get('店舗名')).first()
            if restaurant:
                review_count = item.get('レビュー数', 0)
                restaurant.review_count = int(review_count) if isinstance(review_count, int) else 0
                restaurant.save()

if __name__ == '__main__':
    import_reviews()