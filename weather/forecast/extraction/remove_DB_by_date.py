from .extraction.remove_config import DAYS_COUNT_BACK, table_names
from models import Weekly, Current_Weather
from datetime import datetime, timedelta


def delete_old():
    Weekly.objects.filter(date__lt=datetime.datetime.now() - timedelta(days = DAYS_COUNT_BACK)).delete()
    Current_Weather.objects.filter(date__lt=datetime.datetime.now() - timedelta(days = DAYS_COUNT_BACK)).delete()
