import requests
from datetime import datetime

GENDER = "man"
WEIGHT_KG = "74"
HEIGHT_CM = "177"
AGE = "23"


API_ID = "f72e7d31"
API_KEY = "fde65db7aaf83d374f13ee0d25cc94cb"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/a578bdd9a2a0a797fc4e8383da9193a5/myWorkouts/workouts"


exercise_text = input("무슨 운동 하시나요?: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    }

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()


today_date = datetime.now().strftime('%Y%m%d')
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:    
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise":	exercise["name"].title(),
            "duration":	exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_input)
    print(sheet_response)

    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_input, 
        auth=(
            "sonnyhyunny", 
            "tjrgus8244",
        )
    )

    #Bearer Token Authentication
    bearer_headers = {
    "Authorization": f"Bearer {"sadasdevfvwedcfwxcc"}"
    }
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_input, 
        headers=bearer_headers
    )

    print(sheet_response.text)
