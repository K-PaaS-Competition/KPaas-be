from rest_framework import serializers
from floodRisk.models import FloodRisk


class FloodDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloodRisk
        fields = [
            "id",
            "location",
            "gidChar",
            "gidCode1",
            "gidCode2",
            "depth10Risk",
            "depth20Risk",
            "depth50Risk",
        ]
