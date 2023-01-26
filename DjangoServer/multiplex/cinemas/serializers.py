from rest_framework import serializers
from .models import Cinema

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'

    def create(self, validated_data):
        return Cinema.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Cinema.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass

