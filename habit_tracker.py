import requests
import datetime

USER_NAME = "anuragibt"
USER_TOKEN = "#anuragibt@pixela"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_config = {
    "token": USER_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_config)
# print(response.text)

graph_endpoints = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Book",
    "unit": "No. of lines",
    "type": "int",
    "color": "shibafu"
}
header = {
    "X-USER-TOKEN": USER_TOKEN
}

# response = requests.post(url=graph_endpoints, json=graph_config, headers=header)
# print(response.text)

today = datetime.datetime.now()

record_endpoints = f"{graph_endpoints}/graph1"
record_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2"
}

response = requests.post(url=record_endpoints, json=record_config, headers=header)
print(response.text)
