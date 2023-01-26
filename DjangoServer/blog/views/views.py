from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from blog.views.repositories import ViewRepository
from blog.views.serializers import ViewSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def view(request):
    if request.method == "POST":
        return ViewSerializer().create(request.data)
    elif request.method == "GET":
        return ViewRepository().find_by_id(request.data)
    elif request.method == "PUT":
        return ViewSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return ViewSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def view_list(request):  return ViewRepository().get_all(request.data)
