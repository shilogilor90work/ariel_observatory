from _future import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ariel_observatory.settings')

app = Celery('ariel_observatory')

app.comfig_from_object('django.conf::settings' ,namespace='CELERY')

app.autodiscover_task()