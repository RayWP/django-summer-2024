from django.contrib import admin
from django.urls import path, include
from sentiment_app.urls import urlpatterns as up2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sentiment/', include('sentiment_app.urls')),
] + up2
