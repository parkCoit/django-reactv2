from django.http import JsonResponse
from rest_framework.response import Response

from blog.comments.models import Comment
from blog.comments.serializers import CommentsSerializer


class CommentsRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(CommentsSerializer(Comment.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(CommentsSerializer(Comment.objects.all(), many=True).data)

