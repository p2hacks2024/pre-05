from django.core.management.base import BaseCommand
from myapp.models import HakodateRestaurant

class Command(BaseCommand):
    help = 'Clear all data from HakodateRestaurant table'

    def handle(self, *args, **kwargs):
        HakodateRestaurant.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared HakodateRestaurant table'))
