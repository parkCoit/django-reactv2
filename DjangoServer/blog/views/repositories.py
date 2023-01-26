from django.http import JsonResponse
from rest_framework.response import Response

from blog.views.models import View
from blog.views.serializers import ViewSerializer


class ViewRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(ViewSerializer(View.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(ViewSerializer(View.objects.all(), many=True).data)

