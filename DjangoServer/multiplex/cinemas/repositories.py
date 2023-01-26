from django.http import JsonResponse
from rest_framework.response import Response

from multiplex.cinemas.models import Cinema
from multiplex.cinemas.serializers import CinemaSerializer


class CinemaRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(CinemaSerializer(Cinema.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(CinemaSerializer(Cinema.objects.all(), many=True).data)

