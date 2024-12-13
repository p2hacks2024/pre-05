from django.shortcuts import render
from .models import HakodateRestaurant
import json
import random

def Start_Screen(request):
    return render(request, 'HOME/StartScreen.html')

def screen(request):
    filter_value = request.GET.get('filter', 'all')
    
    if filter_value == 'few':
        restaurants = HakodateRestaurant.objects.filter(review_count__lte=50)
    elif filter_value == 'medium':
        restaurants = HakodateRestaurant.objects.filter(review_count__gt=50, review_count__lte=200)
    elif filter_value == 'many':
        restaurants = HakodateRestaurant.objects.filter(review_count__gt=200, review_count__lte=500)
    elif filter_value == 'very-many':
        restaurants = HakodateRestaurant.objects.filter(review_count__gt=500)
    elif filter_value == 'very-very-many':
        restaurants = HakodateRestaurant.objects.filter(review_count__gt=1000)
    else:
        restaurants = HakodateRestaurant.objects.all()

    # ランダムに10件を抽出
    restaurants = random.sample(list(restaurants), min(len(restaurants), 10))

    fireworks_locations = []
    for restaurant in restaurants:
        #print(f"Restaurant: {restaurant.name}, Latitude: {restaurant.latitude}, Longitude: {restaurant.longitude}")  # デバッグ用ログ
        fireworks_locations.append({
            'name': restaurant.name,
            'latitude': restaurant.latitude,
            'longitude': restaurant.longitude,
            'description': restaurant.address,  # 店の住所を説明として追加
            'review_count': restaurant.review_count  # レビュー数を追加
        })

   #print("Fireworks Locations:", json.dumps(fireworks_locations, indent=2))

    context = {
        'fireworks_locations': json.dumps(fireworks_locations),
    }

    return render(request, 'HOME/Screen.html', context)