from django.urls import re_path as url
from blog.blog_users import views

urlpatterns = [
    url(r'login', views.login),
    url(r'signup', views.signup),
    url(r'user', views.user),
    url(r'list', views.user_list),
    url(r'list/name', views.user_list_by_name)
]
