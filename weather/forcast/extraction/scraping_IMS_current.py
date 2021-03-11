from .IMS_config import current_forcast_site, zone_ariel, future_forcast_site, API_TOKEN
from models import Current_Weather
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
        current_item.update(Rain=str(name_value['Rain']), WSmax=str(name_value['WSmax']), WDmax=str(name_value['WDmax']), WS=str(name_value['WS']),
        WD=str(name_value['WD']), STDwd=str(name_value['STDwd']), TD=str(name_value['TD']), TW=str(name_value['TW']), TDmax=str(name_value['TDmax']),
        TDmin=str(name_value['TDmin']), WS1mm=str(name_value['WS1mm']), WS10mm=str(name_value['Ws10mm']), time=str(name_value['Time']), TG=str(name_value['TG']), RH=str(name_value['RH']))
    else:
        Current_Weather.create(current_time=current_time, Rain=str(name_value['Rain']), WSmax=str(name_value['WSmax']), WDmax=str(name_value['WDmax']), WS=str(name_value['WS']),
        WD=str(name_value['WD']), STDwd=str(name_value['STDwd']), TD=str(name_value['TD']), TW=str(name_value['TW']), TDmax=str(name_value['TDmax']),
        TDmin=str(name_value['TDmin']), WS1mm=str(name_value['WS1mm']), WS10mm=str(name_value['Ws10mm']), time=str(name_value['Time']), TG=str(name_value['TG']), RH=str(name_value['RH']))
    print(name_value)
