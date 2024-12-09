from django.db import models

class HashtagInfo(models.Model):
    hashtag_name = models.CharField(max_length=255)  # ハッシュタグ名
    hashtag_count = models.PositiveIntegerField()    # ハッシュタグ数
    latitude = models.FloatField()                  # 緯度
    longitude = models.FloatField()                 # 経度
    shop_name = models.CharField(max_length=255)     # 店名

    def __str__(self):
        return f"{self.shop_name} ({self.hashtag_name})"
