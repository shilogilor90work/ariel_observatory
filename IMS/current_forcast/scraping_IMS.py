from IMS_config import current_forcast_site, zone_ariel, future_forcast_site, API_TOKEN
import json
import requests
import mysql.connector

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
print(name_value)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shilo",
  database="IMS"
)

mycursor = mydb.cursor()

sql = "INSERT INTO weather (datetime, Rain, WSmax, WDmax, WS, WD, STDwd, TD, TW, TDmax, TDmin, WS1mm, Ws10mm, Time, TG, RH) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

val = (str(name_value['datetime']), str(name_value.get('Rain','')), str(name_value.get('WSmax','')), str(name_value.get('WDmax','')), str(name_value.get('WS','')), str(name_value.get('WD','')), str(name_value.get('STDwd','')), str(name_value.get('TD','')), str(name_value.get('TW','')), str(name_value.get('TDmax','')), str(name_value.get('TDmin','')), str(name_value.get('WS1mm','')), str(name_value.get('Ws10mm','')), str(name_value.get('Time','')), str(name_value.get('TG','')), str(name_value.get('RH','')))
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
