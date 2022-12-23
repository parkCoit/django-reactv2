from django.urls import re_path as url
from dlearn import views

urlpatterns = [
    url(r'iris', views.iris),
    url(r'iris/(?P<req>)$', views.iris),
    url(r'fashion/(?P<id>)$', views.fashion),
    url(r'fashion', views.fashion),
    url(r'number', views.number)
]
