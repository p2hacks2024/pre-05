import json
import os
from django.core.management.base import BaseCommand
from myapp.models import HakodateRestaurant

class Command(BaseCommand):
    help = 'Import Hakodate restaurants from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        
        if not os.path.exists(json_file):
            self.stdout.write(self.style.ERROR(f"Error: The file {json_file} does not exist."))
            return
        
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        for item in data:
            HakodateRestaurant.objects.create(
                name=item.get('店舗名'),
                address=item.get('住所'),
                latitude=item.get('緯度'),
                longitude=item.get('経度'),
                review_count=item.get('レビュー数', 0),
                restaurant_id=item.get('shopid'),
                url_pc=item.get('url', {}).get('pc'),
                logo_image=item.get('ロゴ画像')
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully imported Hakodate restaurants'))
