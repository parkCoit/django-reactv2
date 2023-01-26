from django.urls import re_path as url
from nlp.korean_classify import views

urlpatterns = [
    url(r'korean-classify', views.koreanClassify)
]

