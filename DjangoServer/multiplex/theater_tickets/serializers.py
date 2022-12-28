from rest_framework import serializers
from models import TheaterTicket

class TheaterTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheaterTicket
        fields = '__all__'

