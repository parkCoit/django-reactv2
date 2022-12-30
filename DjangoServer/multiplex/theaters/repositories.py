from django.http import JsonResponse
from rest_framework.response import Response

from multiplex.theaters.models import Theater
from multiplex.theaters.serializers import TheaterSerializer


class TheaterRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(TheaterSerializer(Theater.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(TheaterSerializer(Theater.objects.all(), many=True).data)

