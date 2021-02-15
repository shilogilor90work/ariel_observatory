from IMS_config import current_forcast_site, zone_ariel, future_forcast_site, API_TOKEN
import json
import requests

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



# sites to pull data incase API TOKEN not allowed
#
# x = requests.post(current_forcast_site)
# print(x.json()['data'][zone_ariel])
# print()
# y = requests.post(future_forcast_site+zone_ariel)
# print(y.json())
#
