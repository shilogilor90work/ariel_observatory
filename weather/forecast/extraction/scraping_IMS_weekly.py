from .IMS_weekly_config import current_forecast_site, zone_ariel, future_forecast_site, whether, API_TOKEN
from forecast.models import Weekly
from datetime import datetime
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time

def scrape_IMS_weekly():

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    d = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    url = future_forecast_site + zone_ariel
    print(url)
    d.get(url)
    time.sleep(5)
    text_of_d = d.execute_script("return document.body.innerText;")
    time.sleep(5)
    print(text_of_d)
    # request
    data= json.loads(text_of_d.encode('utf8'))
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
            current_item.update(weather_code=str(single_current_data['weather_code']), weather=str(single_current_data['weather']), temperature=str(single_current_data['temperature']))
        else:
            Weekly.objects.create(forecast_time=current_time, weather_code=str(single_current_data['weather_code']), weather=str(single_current_data['weather']), temperature=str(single_current_data['temperature']))
