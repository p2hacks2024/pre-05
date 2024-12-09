from django.urls import path
from . import views  # viewsからshow_jsonをインポート

urlpatterns = [
    path('show-json/', views.show_json, name='show_json'),  # show_jsonビューにマッピング
]