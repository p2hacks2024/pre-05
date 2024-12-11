from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=255)       # 店舗名
    address = models.TextField()                  # 住所
    latitude = models.FloatField()                # 緯度
    longitude = models.FloatField()               # 経度
    shop_id = models.CharField(max_length=255)    # 店舗ID

    def __str__(self):
        return self.name

class HakodateRestaurant(models.Model):
    name = models.CharField(max_length=255)       # 店舗名
    address = models.TextField()                  # 住所
    latitude = models.FloatField()                # 緯度
    longitude = models.FloatField()               # 経度
    restaurant_id = models.CharField(max_length=255)  # レストランID
    review_count = models.IntegerField(default=0)  # レビュー数を追加

    def __str__(self):
        return self.name