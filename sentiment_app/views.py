from django.shortcuts import render
from django.http import JsonResponse
import joblib
from .forms import SentimentForm, StudentForm
from .models import Student

# 加載模型
model = joblib.load('sentiment_app/movie_review_model.pkl')


def index(request):
    return render(request, 'index.html')


def for_loop_example(request):
    data = [1, 2, 3, 4, 5]
    return render(request, 'sentiment_app/for_loop_example.html', {'data': data})


def select_all_student(request):
    #     return students json array
    students = Student.objects.all()
    student_list = list(students.values())
    return JsonResponse(student_list, safe=False)

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            student = Student(name=name, age=age)
            student.save()

            new_form = StudentForm()
            # get all student
            student_list = Student.objects.all()
            return render(request, 'sentiment_app/create_student.html', {'form': new_form, 'message': 'Student created successfully', 'students': student_list})
    else:
        # get all student
        student_list = Student.objects.all()
        form = StudentForm()
        return render(request, 'sentiment_app/create_student.html', {'form': form, 'students': student_list})



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
