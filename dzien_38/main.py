import requests
import datetime

APP_ID = "<app_id>"
APP_KEY = "<app_key>"

GENDER = "<gender>"
WEIGHT_KG = 0 #Int
HEIGHT_CM = 0 #Int
AGE = 0 #Int

SHEET_NAME = "<sheet_name>"
SHEET = "<sheet>"

nutritionix_natural_language_endpoint = "<endpoint>"

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

#Run 2 miles and walked 3 KM.
data = str(input("Tell me which exercise you did: "))

Parameters = {
    "query": data,
    "gender" : GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE,
}

response = requests.post(nutritionix_natural_language_endpoint, headers=header, json=Parameters)
result = response.json()
print(response.json())

# --------------------- Sheety -------------------

today_date = str(datetime.date.today())
print(today_date)
time = datetime.datetime.now()
time_now = str(time.strftime("%H:%M:%S"))
print(time_now)

for exercise in result["exercises"]:
    exercise_json = {
        SHEET : {
            "date" : today_date,
            "time" : time_now,
            "exercise" : exercise["user_input"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"],
        }
    }

sheety_post_endpoint = "<endpoint>"

sheet_post = requests.post(url = sheety_post_endpoint, json=exercise_json)
print(sheet_post.json())

