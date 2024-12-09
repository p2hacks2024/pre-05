from django.http import JsonResponse

def fetch_trends(request):
    trends = [
        {"lat": 41.768793, "lng": 140.72881, "trend": "函館山夜景", "count": 120},
        {"lat": 41.779567, "lng": 140.725646, "trend": "五稜郭", "count": 80}
    ]
    return JsonResponse(trends, safe=False)
