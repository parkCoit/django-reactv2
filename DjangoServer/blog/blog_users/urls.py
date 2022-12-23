from django.urls import re_path as url
from blog.blog_users import views

urlpatterns = [
    url(r'login', views.login),
    url(r'signup', views.signup),
    url(r'insertdummy', views.insertdummy),
]