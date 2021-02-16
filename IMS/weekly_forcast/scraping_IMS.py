from IMS_weekly_config import current_forcast_site, zone_ariel, future_forcast_site
import json
import requests
import mysql.connector

# URL
url = requests.post(future_forcast_site + zone_ariel)


# request
response = requests.request("POST", url)
# dump data
data= json.loads(response.text.encode('utf8'))
# parse data
temp_day = [day for day in data['data']]
current_data = {}
for day in data['data']:
    for hour in day:
        for specific_time in hour:
            current_data[specific_time[forecast_time]] = {"forecast_time": specific_time["forecast_time"], "weather_code": specific_time["weather_code"], "temperature": specific_time["temperature"], "weather": ""}
            try:
                current_data[specific_time[forecast_time]]["weather"] = whether[specific_time["weather_code"]]

# print, will be converted to send data to DB
print(current_data)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shilo",
    database="IMS"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE weekly_weather (forecast_time VARCHAR(255) , PRIMARY KEY(`forecast_time`) , weather_code VARCHAR(255) , weather VARCHAR(255) , temperature VARCHAR(255)")
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
