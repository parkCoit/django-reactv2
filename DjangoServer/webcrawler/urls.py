from django.urls import re_path as url
from webcrawler import views

urlpatterns = [
    url(r'naver', views.webcrawler),
]
