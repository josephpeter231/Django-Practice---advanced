from celery import shared_task
from django.utils import timezone

@shared_task
def send_reminder_email():
    print("Sending reminder email at", timezone.now())
