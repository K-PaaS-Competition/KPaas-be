from django.db import models
from city.models import City


class SubRegion(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=100, null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    class Meta:
        db_table = "subRegion"

    def __str__(self):
        return self.name
