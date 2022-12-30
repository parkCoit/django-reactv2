from django.http import JsonResponse
from rest_framework.response import Response

from blog.tags.models import Tag
from blog.tags.serializers import TagSerializer


class TagRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(TagSerializer(Tag.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(TagSerializer(Tag.objects.all(), many=True).data)

