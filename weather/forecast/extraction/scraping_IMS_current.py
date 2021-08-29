from .IMS_config import current_forecast_site, zone_ariel, future_forecast_site, API_TOKEN
from forecast.models import Current_Weather
import json
from datetime import datetime
import requests
# import mysql.connector

def scrape_IMS_current():
    # URL API
    url = "https://api.ims.gov.il/v1/Envista/stations/" + zone_ariel + "/data/latest"

    # Token givven by IMS
    headers = {
      'Authorization' : 'ApiToken ' + API_TOKEN
    }
    # request
    response = requests.request("GET", url, headers=headers)
    # dump data
    data= json.loads(response.text.encode('utf8'))
    # parse data
    current_data = data['data'][0]['channels']
    name_value = {current_data[i]['name']: current_data[i]['value'] for i in range(len(current_data))}
    name_value['datetime'] = data['data'][0]['datetime']
    # print, will be converted to send data to DB
    current_time = datetime.strptime(name_value['datetime'][:19], '%Y-%m-%dT%H:%M:%S')

    current_item = Current_Weather.objects.filter(current_time=current_time)
    if current_item.exists():
        current_item.objects.update(rain=str(name_value.get('Rain','')), wsmax=str(name_value.get('WSmax','')), wdmax=str(name_value.get('WDmax','')), ws=str(name_value.get('WS','')),
        wd=str(name_value.get('WD','')), stdwd=str(name_value.get('STDwd','')), td=str(name_value.get('TD','')), tw=str(name_value.get('TW','')), tdmax=str(name_value.get('TDmax','')),
        tdmin=str(name_value.get('TDmin','')), ws1mm=str(name_value.get('WS1mm','')), ws10mm=str(name_value.get('Ws10mm','')), time=str(name_value.get('Time','')), tg=str(name_value.get('TG','')), rh=str(name_value.get('RH','')))
    else:
        Current_Weather.objects.create(current_time=current_time, rain=str(name_value.get('Rain','')), wsmax=str(name_value.get('WSmax','')), wdmax=str(name_value.get('WDmax','')), ws=str(name_value.get('WS','')),
        wd=str(name_value.get('WD','')), stdwd=str(name_value.get('STDwd','')), td=str(name_value.get('TD','')), tw=str(name_value.get('TW','')), tdmax=str(name_value.get('TDmax','')),
        tdmin=str(name_value.get('TDmin','')), ws1mm=str(name_value.get('WS1mm','')), ws10mm=str(name_value.get('Ws10mm','')), time=str(name_value.get('Time','')), tg=str(name_value.get('TG','')), rh=str(name_value.get('RH','')))
    print(name_value)
