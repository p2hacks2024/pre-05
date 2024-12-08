from django.shortcuts import render
import json
from django.http import JsonResponse

def show_json(request):
    # JSONファイルを開く
    with open('data.json', 'r') as file:
        data = json.load(file)

    # JSONの内容を表示
    return JsonResponse(data, safe=False)  # JsonResponseを使ってJSONデータを返す