from django.urls import path
from . import views

urlpatterns = [
    path('api/trends/', views.fetch_trends, name='fetch_trends'),
]
