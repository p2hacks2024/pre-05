from django.shortcuts import render, get_object_or_404
from .models import HakodateRestaurant

def hakodate_restaurant_location(request):
    restraunt = get_object_or_404(HakodateRestaurant, name='たろ吉')
    context = {
        'name': restraunt.name,
        'latitude': restraunt.latitude,
        'longitude': restraunt.longitude,
    }
    return render(request, 'HOME/StartScreen.html', context)