import requests
from datetime import datetime


MY_LAT = 10.765080
MY_LNG = 79.633560

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if response.status_code == 404:
# #     raise Exception("That Resource not Exists")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorised to access")
# response.raise_for_status()
#
# data = response.json()
# print(data)
# data1 = response.json()["iss_position"]["longitude"]
# print(data1)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)