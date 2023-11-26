from django.db import models
from city.models import City


# 30분 강우량을 저장
class Rain(models.Model):
    subRegion = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    regionName = models.CharField(max_length=100, null=False)
    sum = models.FloatField(default=0)
    FirstAdded = models.FloatField(default=0)
    AddedCount = models.IntegerField(default=0)

    class Meta:
        db_table = "rain"

    def __str__(self):
        return self.regionName + " " + sum
