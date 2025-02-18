import requests
from datetime import datetime

# Nutritionix API Credentials
APP_ID = "66780314"
API_KEY = "e50566f828cd3570f61c3149d5124f0b"

GENDER = "MALE"
WEIGHT_KG = 70
HEIGHT_CM = 173
AGE = 20

# Nutritionix Endpoint
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

TOKEN = "TmlkaGlzaDpOaWRoaXNoMTgxMA=="

# Sheety Endpoint and Authorization
sheety_endpoint = "https://api.sheety.co/f89c5faa0323c1b2bb1c3c838fe5af5c/myWorkouts/workouts"
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
