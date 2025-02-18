import requests
from datetime import datetime

# Nutritionix API Credentials
APP_ID = "YOUR API ID"
API_KEY = "YOUR API KEY"

GENDER = "male/ female"
WEIGHT_KG = "WEIGHT"
HEIGHT_CM = "HEIGHT"
AGE = "AGE"

# Nutritionix Endpoint
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

TOKEN = "TOKEN GIVEN"

# Sheety Endpoint and Authorization
sheety_endpoint = "SHEETY END POINTS"
sheety_headers = {
    "Authorization": f"Basic {TOKEN}"  # Add your Sheety token
}

# Input Exercise Data
exercise_text = input("Tell me which exercises you did: ")

# Headers and Parameters for Nutritionix
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

# Fetch Exercise Data from Nutritionix
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# Process Nutritionix Response and Post to Sheety
for exercise in result["exercises"]:
    exercise_name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    # Format Date
    today = datetime.now().strftime("%Y-%m-%d")

    # Sheety Data Payload
    sheety_payload = {
        "workout": {
            "date": today,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories
        }
    }

    # Post Data to Sheety
    sheety_response = requests.post(sheety_endpoint, json=sheety_payload, headers=sheety_headers)
    print(sheety_response.text)

print("Workout logged to Sheety!")
