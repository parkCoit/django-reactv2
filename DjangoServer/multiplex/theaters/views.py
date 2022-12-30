from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from multiplex.theaters.repositories import TheaterRepository
from multiplex.theaters.serializers import TheaterSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def theater(request):
    if request.method == "POST":
        return TheaterSerializer().create(request.data)
    elif request.method == "GET":
        return TheaterRepository().find_by_id(request.data)
    elif request.method == "PUT":
        return TheaterSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return TheaterSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def theater_list(request):  return TheaterRepository().get_all(request.data)