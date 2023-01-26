from rest_framework import serializers
from .models import TheaterTicket

class TheaterTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheaterTicket
        fields = '__all__'

    def create(self, validated_data):
        return TheaterTicket.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        TheaterTicket.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass


