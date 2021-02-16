from IMS_weekly_config import current_forcast_site, zone_ariel, future_forcast_site, whether
import json
import requests
import mysql.connector

# request
response = requests.post(future_forcast_site + zone_ariel)
# dump data
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

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shilo",
    database="IMS"
)

mycursor = mydb.cursor()

sql = "INSERT INTO weekly_weather (forecast_time, weather_code, weather, temperature) VALUES (%s, %s, %s, %s)"

for single_current_data in current_data:
    val = (str(single_current_data['forecast_time']), str(single_current_data['weather_code']), str(single_current_data['weather']), str(single_current_data['temperature']))
    mycursor.execute(sql, val)

mydb.commit()


# sites to pull data incase API TOKEN not allowed
#
# x = requests.post(current_forcast_site)
# print(x.json()['data'][zone_ariel])
# print()
# y = requests.post(future_forcast_site+zone_ariel)
# print(y.json())
#
