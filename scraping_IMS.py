from IMS_config import current_forcast_site, zone_ariel, future_forcast_site
import requests

x = requests.get(current_forcast_site)
print(x.json()['data'][zone_ariel])
print()
y = requests.get(future_forcast_site+zone_ariel)
print(y.json())
