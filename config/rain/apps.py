from django.apps import AppConfig
from django.conf import settings


class RainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "rain"


# class RainConfig(AppConfig):
#     default_auto_field = "django.db.models.BigAutoField"
#     name = "rain"

#     def ready(self):
#         if settings.SCHEDULER_DEFAULT:
#             from . import operator

#             operator.start()
