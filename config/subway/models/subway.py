from django.db import models
from city.models import City


# Create your models here.
class Subway(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    city = models.ForeignKey(City, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    line = models.CharField(max_length=100)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    class Meta:
        db_table = "subway"

    def __str__(self):
        return self.stationName
