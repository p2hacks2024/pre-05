from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('shop-location/', views.shop_location, name='shop_location'),
]