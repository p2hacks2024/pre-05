from django.contrib import admin
from .models import Shop, HakodateRestaurant  # HakodateRestaurantをインポート

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latitude', 'longitude', 'shop_id')

@admin.register(HakodateRestaurant)
class HakodateRestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latitude', 'longitude', 'restaurant_id', 'review_count','pickup_review','url_pc','logo_image')  # review_countを追加