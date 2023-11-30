from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    maxLat = models.FloatField(default=0)
    maxLng = models.FloatField(default=0)
    minLat = models.FloatField(default=0)
    minLng = models.FloatField(default=0)

    class Meta:
        db_table = "city"

    def __str__(self):
        return self.name
