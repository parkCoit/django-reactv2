from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from multiplex.theater_tickets.repositories import TheaterTicketRepository
from multiplex.theater_tickets.serializers import TheaterTicketSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def teater_ticket(request):
    if request.method == "POST":
        return TheaterTicketSerializer().create(request.data)
    elif request.method == "GET":
        return TheaterTicketRepository().find_by_id(request.data)
    elif request.method == "PUT":
        return TheaterTicketSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return TheaterTicketSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def teater_ticket_list(request):  return TheaterTicketRepository().get_all(request.data)
