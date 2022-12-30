from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from multiplex.showtimes.repositories import ShowtimeRepository
from multiplex.showtimes.serializers import ShowtimeSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def showtime(request):
    if request.method == "POST":
        return ShowtimeSerializer().create(request.data)
    elif request.method == "GET":
        return ShowtimeRepository().find_by_id(request.data)
    elif request.method == "PUT":
        return ShowtimeSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return ShowtimeSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def showtime_list(request):  return ShowtimeRepository().get_all(request.data)

