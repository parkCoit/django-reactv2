from django.http import JsonResponse
from rest_framework.response import Response

from multiplex.theater_tickets.models import TheaterTicket
from multiplex.theater_tickets.serializers import TheaterTicketSerializer


class TheaterTicketRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(TheaterTicketSerializer(TheaterTicket.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(TheaterTicketSerializer(TheaterTicket.objects.all(), many=True).data)

