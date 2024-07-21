from django.urls import path, include
from .views import analyze_sentiment, index

urlpatterns = [
    path('', index, name='index'),
    path('analyze/', analyze_sentiment, name='analyze_sentiment'),
]
