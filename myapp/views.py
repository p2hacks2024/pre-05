from django.shortcuts import render, get_object_or_404
from .models import Shop

def shop_location(request):
    shop = get_object_or_404(Shop, name='屋台 ライダーキック')
    context = {
        'name': shop.name,
        'latitude': shop.latitude,
        'longitude': shop.longitude,
    }
    return render(request, 'HOME/Screen.html', context)