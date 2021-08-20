from models import Weekly, Current_Weather
from datetime import datetime, timedelta


def delete_old():
    Weekly.objects.filter(date__lt=datetime.datetime.now() - timedelta(days = 3)).delete()
    Current_Weather.objects.filter(date__lt=datetime.datetime.now() - timedelta(days = 3)).delete()
