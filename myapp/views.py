from django.shortcuts import render
from .models import HakodateRestaurant
import json

def Start_Screen(request):
    return render(request, 'HOME/StartScreen.html')

def screen(request):
    # 1000以上のレビュー数を持つレストランをフィルタリング
    restaurants = HakodateRestaurant.objects.filter(review_count__gte=1000)
    print(f"Retrieved {restaurants.count()} restaurants with 1000 or more reviews")  # デバッグ用ログ


    fireworks_locations = []
    for restaurant in restaurants:
        print(f"Restaurant: {restaurant.name}, Latitude: {restaurant.latitude}, Longitude: {restaurant.longitude}")  # デバッグ用ログ
        fireworks_locations.append({
            'name': restaurant.name,
            'latitude': restaurant.latitude,
            'longitude': restaurant.longitude
        })

    print("Fireworks Locations:", json.dumps(fireworks_locations, indent=2))

    context = {
        'fireworks_locations': json.dumps(fireworks_locations),
    }

    return render(request, 'HOME/Screen.html', context)