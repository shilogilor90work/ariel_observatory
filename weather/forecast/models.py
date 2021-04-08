

from datetime import datetime
from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User


class Weekly(models.Model):
    """Weekly
    """

    HELP_forecast = 'time for prediction'
    HELP_CODE = 'IMS code number'
    HELP_TEMPERATURE = 'temperature'
    HELP_WEATHER = 'translating the IMS code to words'

    forecast_time = models.DateTimeField(unique=True, help_text=HELP_forecast)

    weather_code = models.CharField(max_length=64, help_text=HELP_CODE)

    temperature = models.CharField(max_length=64, help_text=HELP_TEMPERATURE)

    weather = models.CharField(max_length=128, help_text=HELP_WEATHER)

    def __str__(self):
        return f"{self.forecast_time} -- {self.weather_code} -- {self.temperature} -- {self.weather}"


class Current_Weather(models.Model):
    """Current_Weather
    """

    HELP_forecast = 'time for prediction'
    HELP_CODE = 'needs to change'
    current_time = models.DateTimeField(unique=True, help_text=HELP_forecast)

    Rain = models.CharField(max_length=64, help_text=HELP_CODE)
    WSmax = models.CharField(max_length=64, help_text=HELP_CODE)
    WDmax = models.CharField(max_length=64, help_text=HELP_CODE)
    WS = models.CharField(max_length=64, help_text=HELP_CODE)
    WD = models.CharField(max_length=64, help_text=HELP_CODE)
    STDwd = models.CharField(max_length=64, help_text=HELP_CODE)
    TD = models.CharField(max_length=64, help_text=HELP_CODE)
    TW = models.CharField(max_length=64, help_text=HELP_CODE)
    TDmax = models.CharField(max_length=64, help_text=HELP_CODE)
    TDmin = models.CharField(max_length=64, help_text=HELP_CODE)
    WS1mm = models.CharField(max_length=64, help_text=HELP_CODE)
    WS10mm = models.CharField(max_length=64, help_text=HELP_CODE)
    time = models.CharField(max_length=64, help_text=HELP_CODE)
    TG = models.CharField(max_length=64, help_text=HELP_CODE)
    RH = models.CharField(max_length=64, help_text=HELP_CODE)


    def __str__(self):
        return f"{self.current_time} -- {self.Rain} -- {self.WSmax} -- {self.WDmax} -- \
            {self.WS} -- {self.WD} -- {self.STDwd} -- {self.TD} -- \
            {self.TW} -- {self.TDmax} -- {self.TDmin} -- {self.WS1mm} -- \
            {self.WS10mm} -- {self.time} -- {self.TG} -- {self.RH}"



class Rules(models.Model):
    """Rules
    """

    Help_status = 'the status color'
    HELP_min_rain = 'min rain'
    HELP_max_rain = 'max rain'
    HELP_min_wsmax = 'min wsmax'
    HELP_max_wsmax = 'max wsmax'
    HELP_min_wdmax = 'min wdmax'
    HELP_max_wdmax = 'max wdmax'
    HELP_min_ws = 'min ws'
    HELP_max_ws = 'max ws'
    HELP_min_wd = 'min wd'
    HELP_max_wd = 'max wd'
    HELP_min_wsmax = 'min wsmax'
    HELP_max_wsmax = 'max wsmax'
    HELP_min_stdwd = 'min stdwd'
    HELP_max_stdwd = 'max stdwd'
    HELP_min_td = 'min td'
    HELP_max_td = 'max td'
    HELP_min_tw = 'min tw'
    HELP_max_tw = 'max tw'
    HELP_min_tdmax = 'min tdmax'
    HELP_max_tdmax = 'max tdmax'
    HELP_min_tdmin = 'min tdmin'
    HELP_max_tdmin = 'max tdmin'
    HELP_min_ws1mm = 'min ws1mm'
    HELP_max_ws1mm = 'max ws1mm'
    HELP_min_ws10mm = 'min ws10mm'
    HELP_max_ws10mm = 'max ws10mm'
    HELP_min_time = 'min time'
    HELP_max_time = 'max time'
    HELP_min_tg = 'min tg'
    HELP_max_tg = 'max tg'
    HELP_min_rh = 'min rh'
    HELP_max_rh = 'max rh'

    status_type = models.CharField(max_length=64, help_text=Help_status)

    min_rain = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_rain)
    max_rain = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_rain)

    min_wsmax = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_wsmax)
    max_wsmax = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_wsmax)

    min_wdmax = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_wdmax)
    max_wdmax = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_wdmax)

    min_ws = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_ws)
    max_ws = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_ws)

    min_wd = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_wd)
    max_wd = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_wd)

    min_stdwd = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_stdwd)
    max_stdwd = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_stdwd)

    min_td = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_td)
    max_td = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_td)

    min_tw = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_tw)
    max_tw = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_tw)

    min_tdmax = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_tdmax)
    max_tdmax = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_tdmax)

    min_tdmin = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_tdmin)
    max_tdmin = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_tdmin)

    min_ws1mm = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_ws1mm)
    max_ws1mm = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_ws1mm)

    min_ws10mm = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_ws10mm)
    max_ws10mm = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_ws10mm)

    min_time = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_time)
    max_time = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_time)

    min_tg = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_tg)
    max_tg = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_tg)

    min_rh = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_min_rh)
    max_rh = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_max_rh)

    weather = models.CharField(max_length=64, help_text=Help_status)


    def __str__(self):
        return f"status_type {self.status_type} - name, min, max : \nrain, {self.min_rain}, {self.max_rain} \nrwsmax, {self.min_wsmax}, {self.max_wsmax} \
        \nwdmax, {self.min_wdmax}, {self.max_wdmax} \nws, {self.min_ws}, {self.max_ws} \nwsmax, {self.min_wsmax}, {self.max_wsmax} \
        \nwd, {self.min_wd}, {self.max_wd} \nstdwd, {self.min_stdwd}, {self.max_stdwd} \ntd, {self.min_td}, {self.max_td}\
        \ntw, {self.min_tw}, {self.max_tw} \ntdmax, {self.min_tdmax}, {self.max_tdmax} \ntdmin, {self.min_tdmin}, {self.max_tdmin}\
        \nws1mm, {self.min_ws1mm}, {self.max_ws1mm} \nws10mm, {self.min_ws10mm}, {self.max_ws10mm} \ntime, {self.min_time}, {self.max_time} \
        \ntg, {self.min_tg}, {self.max_tg} \nrh, {self.min_rh}, {self.max_rh} \nweather, {self.weather}, {self.max_ws1mm} "
