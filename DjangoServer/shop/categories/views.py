from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from shop.categories.repositories import CategoryRepository
from shop.categories.serializers import CategorySerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def category(request):
    if request.method == "POST":
        return CategorySerializer().create(request.data)
    elif request.method == "GET":
        return CategoryRepository().find_by_id(request.data)
    elif request.method == "PUT":
        return CategorySerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return CategorySerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def category_list(request):  return CategoryRepository().get_all(request.data)

