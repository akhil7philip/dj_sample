from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import functools


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings.local')

app = Celery('app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

REDIS_CLIENT = app.backend.client  # re-use result backend Redis client
# REDIS_CLIENT = os.environ.get('CELERY_BROKER_URL', 'amqp://localhost')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))