from django.http import JsonResponse
from rest_framework.response import Response

from multiplex.movies.models import Movie
from multiplex.movies.serializers import MovieSerializer


class MovieRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(MovieSerializer(Movie.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(MovieSerializer(Movie.objects.all(), many=True).data)

