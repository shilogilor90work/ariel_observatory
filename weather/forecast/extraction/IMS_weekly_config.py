# we used the file from https://ims.gov.il/sites/default/files/2020-08/CodesForIMSWebSite_1.pdf to make this file
whether = {
    '1010':"Sandstorms",
    '1020':"Thunderstorms",
    '1060':"Snow",
    '1070':"Light snow",
    '1080':"Sleet",
    '1140':"Rainy",
    '1160':"Fog",
    '1220':"Partly cloudy",
    '1230':"Cloudy",
    '1250':"Clear",
    '1260':"Windy",
    '1270':"Muggy",
    '1300':"Frost",
    '1310':"Hot",
    '1320':"Cold",
    '1510':"Stormy",
    '1530':"Partly cloudy, possible rain",
    '1520':"Heavy snow",
    '1540':"Cloudy, possible rain",
    '1560':"Cloudy, light rain",
    '1570':"Dust",
    '1580':"Extremely hot ",
    '1590':"Extremely cold"
}
channel = {
    'BP':"BP",
    'DiffR':"disporsed Radiation",
    'Grad':"Global Radiation",
    'NIP':"NIP",
    'Rain':"Rain in mm",
    'Rh':"Range of Humidity",
    'STDwd':"STD of Wind Direction",
    'TD':"Temperature Degree",
    'TDmax':"Temperature Degree Max",
    'TDmin':"Temperature Degree Min",
    'TG':"Temperature Degree by Ground",
    'Time':"Time hhmm",
    'WD':"Wind Direction",
    'WDmax':"Wind Direction Max",
    'WS':"Wind Speed",
    'Ws10mm':"Ws10mm",
    'WS1mm':"WS1mm",
    'WSmax':"WSmax"
}

API_TOKEN = "f058958a-d8bd-47cc-95d7-7ecf98610e47"
current_forecast_site = "https://ims.gov.il/he/now_analysis"
#lid 73
zone_ariel = "21"
future_forecast_site = "https://ims.gov.il/he/forecast_data/"
CHROMEDRIVER_PATH = "/home/ec2-user/ariel_observatory/chromedriver"
