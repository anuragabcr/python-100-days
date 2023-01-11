import requests

location = requests.get(url="http://api.open-notify.org/iss-now.json").json()
print(location['iss_position']['longitude'])