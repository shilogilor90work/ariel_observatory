from models import Weekly, Current_Weather
from datetime import datetime, timedelta


def delete_old():
    DAYS_COUNT_BACK = 3
    Weekly.objects.filter(date__lt=datetime.datetime.now() - timedelta(days = DAYS_COUNT_BACK)).delete()
    Current_Weather.objects.filter(date__lt=datetime.datetime.now() - timedelta(days = DAYS_COUNT_BACK)).delete()
