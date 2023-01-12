import requests

OWN_WEBSITE = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "a655f792425fb01dc35997485821387a"

parameters = {
    "lat": 13.037430,
    "lon": 77.647830,
    # "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY,
}

response = requests.get(OWN_WEBSITE, params=parameters)
response.raise_for_status()
print(response.json())