import requests, datetime,os

GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 184
AGE = 25
Application_ID = os.environ.get("Application_ID")
Application_Keys = os.environ.get("Application_Keys")

app_link = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = (
    "https://api.sheety.co/3433f1cc0c04e3c800e561ff11e8e9d4/workoutTracking/workouts"
)
headers = {
    "x-app-id": Application_ID,
    "x-app-key": Application_Keys,
}
USER_sheety = os.environ.get("USER_sheety")
PASS_sheety = os.environ.get("PASS_sheety")
exercise_text = input("Tell me which exercises you did: ")
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
now = datetime.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

response = requests.post(url=app_link, json=parameters, headers=headers)
data = response.json()
exercise_data = data["exercises"]
for exercise in exercise_data:
    workouts = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response1 = requests.post(url=sheety_endpoint, json=workouts, auth=(USER_sheety, PASS_sheety))
    print(response1.text)
