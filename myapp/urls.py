from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('hakodate_restaurant/', views.hakodate_restaurant_location, name='hakodate_restaurant_location'),
    path('screen/', views.screen, name='screen'),
]