from .IMS_weekly_config import current_forecast_site, zone_ariel, future_forecast_site, whether, API_TOKEN
from forecast.models import Weekly
from datetime import datetime
import json
import requests

def scrape_IMS_weekly():
    url = future_forecast_site + zone_ariel
    # Token givven by IMS
    headers = {
      'Authorization' : 'ApiToken ' + API_TOKEN
    }
    # request
    response = requests.request("GET", url, headers=headers)
    data= json.loads(response.text.encode('utf8'))
    # parse data
    current_data = []
    for day in list(data['data'].values()):
        for hour in list(day["hourly"].values()):
            temp = {"forecast_time": str(hour["forecast_time"]), "weather_code": str(hour["weather_code"]), "temperature": str(hour["temperature"]), "weather": ""}
            try:
                temp["weather"] = whether[str(hour["weather_code"])]
            except:
                print("error parsing weather code")
            current_data.append(temp)

    for single_current_data in current_data:
        current_time = datetime.strptime(single_current_data['forecast_time'][:19], '%Y-%m-%d %H:%M:%S')
        current_item = Weekly.objects.filter(forecast_time=current_time)
        if current_item.exists():
            current_item.objects.update(weather_code=str(single_current_data['weather_code']), weather=str(single_current_data['weather']), temperature=str(single_current_data['temperature']))
        else:
            Weekly.objects.create(forecast_time=current_time, weather_code=str(single_current_data['weather_code']), weather=str(single_current_data['weather']), temperature=str(single_current_data['temperature']))
