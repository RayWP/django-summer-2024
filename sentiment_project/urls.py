from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from sentiment_app.urls import urlpatterns as sentiment_app_url
import sentiment_app.views
from sentiment_app.views import for_loop_example as loop
urlpatterns = [
    path('', sentiment_app.views.index), # you can directly call the function
    path('student/', sentiment_app.views.create_student),
    path('loop',loop), # use an alias
    path('admin/', admin.site.urls), # django's default urls
    path('sentiment/', include(sentiment_app_url)), # include the urls from sentiment_app
]
