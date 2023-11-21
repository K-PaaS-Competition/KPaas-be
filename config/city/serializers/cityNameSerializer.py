from rest_framework import serializers
from city.models import City


class CityNameSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
