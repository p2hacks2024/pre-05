from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('hakodate_restaurant/', views.Start_Screen, name='Start_Screen'),
    path('screen/', views.screen, name='screen'),
]