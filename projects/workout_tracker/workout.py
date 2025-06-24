import requests
GENDER = "male"
WEIGHT_KG = 72
HEIGHT_CM = 175
AGE = 23
APP_ID = "your_app_id"
API_KEY = "your_api_key"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
query = input("Tell me which exercises you did: ")
params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(exercise_endpoint, json=params, headers=headers)
print(response.json())