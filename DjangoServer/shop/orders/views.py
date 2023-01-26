from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from shop.orders.repositories import OrderRepository
from shop.orders.serializers import OrderSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def order(request):
    if request.method == "POST":
        return OrderSerializer().create(request.data)
    elif request.method == "GET":
        return OrderRepository().find_by_id(request.data)
    elif request.method == "PUT":
        return OrderSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return OrderSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def order_list(request):  return OrderRepository().get_all(request.data)


