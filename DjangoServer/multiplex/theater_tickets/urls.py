from django.urls import re_path as url
from multiplex.theater_tickets import views

urlpatterns = [
    url(r'teater-ticket', views.teater_ticket),
    url(r'list', views.teater_ticket_list),
]