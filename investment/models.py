from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    investment_preferences = models.TextField()

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    purchase_price = models.FloatField()
    current_price = models.FloatField()

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    published_at = models.DateTimeField()

class AIRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
