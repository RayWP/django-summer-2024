from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from sentiment_app.urls import urlpatterns as up2

urlpatterns = [
] + up2
