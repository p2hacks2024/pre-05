from django.shortcuts import render, get_object_or_404
from .models import HakodateRestaurant

def Start_Screen(request):
    return render(request, 'HOME/StartScreen.html')

def screen(request):
    restaurant = get_object_or_404(HakodateRestaurant, name='たろ吉')
    context = {
        'name': restaurant.name,
        'latitude': restaurant.latitude,
        'longitude': restaurant.longitude,
    }
    return render(request, 'HOME/Screen.html', context)