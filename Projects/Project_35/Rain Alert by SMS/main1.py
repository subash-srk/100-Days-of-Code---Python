# Rain Alert API
import requests
from twilio.rest import Client

account_sid = ""
auth_token = ""


end_point = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""

weather_params = {
    "lat": 29.749020,
    "lon": -94.834953,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(end_point, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella ☔",
        from_='',
        to=''
    )
    print(message.status)


