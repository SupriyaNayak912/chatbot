from django.urls import path
from .views import get_stock_data

urlpatterns = [
    path('api/stock/<str:symbol>/', get_stock_data),
    path('api/news/', get_finance_news),
    path('api/ai-recommendation/<int:user_id>/', get_ai_recommendation),


]
