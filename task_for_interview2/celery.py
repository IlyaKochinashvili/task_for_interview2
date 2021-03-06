import os
import django
from celery import Celery

from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_for_interview2.settings')
django.setup()
app = Celery('task_for_interview2')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
