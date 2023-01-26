from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from blog.tags.repositories import TagRepository
from blog.tags.serializers import TagSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def tag(request):
    if request.method == "POST":
        return TagSerializer().create(request.data)
    elif request.method == "GET":
        return TagRepository().find_by_id(request.data)
    elif request.method == "PUT":
        return TagSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return TagSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def tag_list(request):  return TagRepository().get_all()

