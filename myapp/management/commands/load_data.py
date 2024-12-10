import json
from django.core.management.base import BaseCommand
from myapp.models import Shop  # Replace Restaurant with Shop

class Command(BaseCommand):
    help = 'Load data from hakodate_restaurants.json into the database'

    def handle(self, *args, **kwargs):
        file_path = 'C:/Users/Owner/Documents/開発_hac2/pre-05/hakodate_restaurants.json'
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                Shop.objects.create(**item)  # Replace Restaurant with Shop
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))