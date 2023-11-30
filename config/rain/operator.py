from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from .views import RainData
import requests


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "djangojobstore")
    register_events(scheduler)

    @scheduler.scheduled_job("cron", minute="*", name="test")
    def auto_check():
        requests.get("http://localhost:8000/city/get?name=seoul")

    scheduler.start()
