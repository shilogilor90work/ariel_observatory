from _future import absolute_import, unicode_literals

from celery import shared_task

@shared_task
def add(x, y):
	return 1+2