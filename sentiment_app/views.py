from django.shortcuts import render
from django.http import JsonResponse
import joblib
from .forms import SentimentForm

# 加載模型
model = joblib.load('sentiment_app/movie_review_model.pkl')

def index(request):
    return render(request, 'index.html')

def for_loop_example(request):
    data = [1, 2, 3, 4, 5]
    return render(request, 'sentiment_app/for_loop_example.html', {'data': data})

def analyze_sentiment(request):
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            prediction = model.predict([text])[0]
            sentiment = 'Positive' if prediction == 'pos' else 'Negative'
            return render(request, 'sentiment_app/result.html', {'form': form, 'sentiment': sentiment})
    else:
        form = SentimentForm()
    return render(request, 'sentiment_app/form.html', {'form': form})
