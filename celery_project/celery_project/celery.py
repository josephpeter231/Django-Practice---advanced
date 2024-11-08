from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app = Celery('celery_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Add this to run periodic tasks
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from reminder.tasks import send_reminder_email
    sender.add_periodic_task(60.0, send_reminder_email.s(), name='send reminder every 1 minute')
