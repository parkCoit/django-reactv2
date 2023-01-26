from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from blog.comments.repositories import CommentsRepository
from blog.comments.serializers import CommentsSerializer

@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def comment(request):
    if request.method == "POST":
        return CommentsSerializer().create(request.data)
    elif request.method == "GET":
        return CommentsRepository().find_by_id(request.data)
    elif request.method == "PUT":
        return CommentsSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return CommentsSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def comment_list(request):  return CommentsRepository().get_all(request.data)

