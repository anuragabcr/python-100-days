import requests
from datetime import datetime

date = datetime.now().date()
time = datetime.now().time()
time = str(time).split('.')[0]

APP_ID = "cfcb5005"
API_KEY = "b1f07ec5f2efb86acedbd6d9fbbad8ae"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

exercise_config = {
    "query": input("Enter the exercise you did: ")
}

response = requests.post(url=exercise_endpoint, headers=exercise_header, json=exercise_config)
response.raise_for_status()
exercise_data = response.json()['exercises']

sheety_endpoint = "https://api.sheety.co/86bdf17eb71bd6613caa8796b6c0ee36/workouts/workouts"
header = {
    "Content-Type": "application/json"
}

for exercise in exercise_data:
    sheety_config = {
        "workout": {
            "Date": str(date),
            "Time": str(time),
            "Exercise": exercise['user_input'],
            "Duration": exercise['duration_min'],
            "Calories": exercise['nf_calories'],
        }
    }
    print(sheety_config)
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_config, headers=header)
    print(sheety_response.text)

