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
    review_count = models.IntegerField(default=0)  # レビュー数を追加
    pickup_review = models.TextField(null=True, blank=True, max_length=1000)  # 長さ制限を追加
    restaurant_id = models.CharField(max_length=255)     # 店舗ID
    url_pc = models.URLField(default='https://example.com')  # URL (PC)
    logo_image = models.URLField(default='https://imgfp.hotp.jp/IMGH/70/08/P033307008/P033307008_69.jpg')  # ロゴ画像

    def __str__(self):
        return self.name