"""

Shilo Gilor.
xFind
"""

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Weekly(models.Model):
    """Weekly
    """

    HELP_FORCAST = 'time for prediction'
    HELP_CODE = 'IMS code number'
    HELP_TEMPERATURE = 'temperature'
    HELP_WEATHER = 'translating the IMS code to words'

    forcast_time = models.DateTimeField(unique=True, help_text=HELP_FORCAST)

    weather_code = models.CharField(max_length=64, help_text=HELP_CODE)

    temperature = models.CharField(max_length=64, help_text=HELP_TEMPERATURE)

    weather = models.CharField(max_length=128, help_text=HELP_WEATHER)

    def __str__(self):
        return f"{self.forcast_time} -- {self.weather_code} -- {self.temperature} -- {self.weather}"


class Current_Weather(models.Model):
    """Current_Weather
    """

    current_time = models.DateTimeField(unique=True, help_text=HELP_FORCAST)

    rain = models.CharField(max_length=64, help_text=HELP_CODE)
    WSmax = models.CharField(max_length=64, help_text=HELP_CODE)
    WDmax = models.CharField(max_length=64, help_text=HELP_CODE)
    WS = models.CharField(max_length=64, help_text=HELP_CODE)
    WD = models.CharField(max_length=64, help_text=HELP_CODE)
    STDwd = models.CharField(max_length=64, help_text=HELP_CODE)
    TD = models.CharField(max_length=64, help_text=HELP_CODE)
    Tw = models.CharField(max_length=64, help_text=HELP_CODE)
    TDmax = models.CharField(max_length=64, help_text=HELP_CODE)
    TDmin = models.CharField(max_length=64, help_text=HELP_CODE)
    WS1mm = models.CharField(max_length=64, help_text=HELP_CODE)
    WS10mm = models.CharField(max_length=64, help_text=HELP_CODE)
    time = models.CharField(max_length=64, help_text=HELP_CODE)
    TG = models.CharField(max_length=64, help_text=HELP_CODE)
    RH = models.CharField(max_length=64, help_text=HELP_CODE)


    def __str__(self):
        return f"{self.current_time} -- {self.rain} -- {self.WSmax} -- {self.WDmax} -- \
            {self.WS} -- {self.WD} -- {self.STDwd} -- {self.TD} -- \
            {self.Tw} -- {self.TDmax} -- {self.TDmin} -- {self.WS1mm} -- \
            {self.WS10mm} -- {self.time} -- {self.TG} -- {self.RH}"
