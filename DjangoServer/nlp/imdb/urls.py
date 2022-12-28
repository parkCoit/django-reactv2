from django.urls import re_path as url
from nlp.imdb import views

urlpatterns = [
    url(r'imdb', views.imdb)
]

