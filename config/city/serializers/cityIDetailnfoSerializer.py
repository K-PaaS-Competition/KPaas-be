from rest_framework import serializers
from city.models import City


class CityDetailInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            "id",
            "name",
            "maxLat",
            "maxLng",
            "minLat",
            "minLng",
        ]
