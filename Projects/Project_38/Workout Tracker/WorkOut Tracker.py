# Workout Tracker
import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""
USER = ""
PASSWORD = ""

WEIGHT_KG = 80
HEIGHT_CM = 181.1
AGE = 21
GENDER = "male"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = ""

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, data=parameters, headers=headers)
result = response.json()

time_now = datetime.now().strftime("%X")
date_now = datetime.now().strftime("%d/%m/%Y")

sheet_params = {}
for exercise in result["exercises"]:
    sheet_params = {
        "workout": {
            "date": date_now,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheet_endpoint, json=sheet_params, auth=(USER,PASSWORD))
print(sheet_response.text)
