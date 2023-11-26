from django.apps import AppConfig
from django.conf import settings


class FloodRiskConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "floodRisk"


class RainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "loadFloodRisk"

    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from . import operator

            operator.start()
