from django.db import models
from city.models import City


class FloodRisk(models.Model):
    city = models.ForeignKey(City, null=False, on_delete=models.CASCADE, default=1)
    location = models.CharField(max_length=100)
    gidChar = models.CharField(max_length=100)
    gidCode1 = models.IntegerField()
    gidCode2 = models.IntegerField()
    depth10Risk = models.FloatField()
    depth20Risk = models.FloatField()
    depth50Risk = models.FloatField()

    class Meta:
        db_table = "floodRisk"

    def __str__(self):
        return f"{self.gidChar} {self.gidCode1} {self.gidCode2}"
