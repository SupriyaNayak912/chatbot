import requests
from django.http import JsonResponse

ALPHA_VANTAGE_API_KEY = "your_alpha_vantage_api_key"

def get_stock_data(request, symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

def get_finance_news(request):
    url = "https://newsapi.org/v2/everything?q=finance&apiKey=your_newsapi_key"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

UPTIQ_AI_API_URL = "your_uptiq_ai_endpoint"

def get_ai_recommendation(request, user_id):
    response = requests.post(UPTIQ_AI_API_URL, json={"user_id": user_id})
    return JsonResponse(response.json())

