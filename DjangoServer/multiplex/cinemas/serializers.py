from rest_framework import serializers
from models import Cinemas

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinemas
        fields = '__all__'

