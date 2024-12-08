
# Register your models here.
from django.contrib import adminpython 
from .models import HashtagInfo

@admin.register(HashtagInfo)
class HashtagInfoAdmin(admin.ModelAdmin):
    list_display = ('hashtag_name', 'hashtag_count', 'shop_name', 'latitude', 'longitude')