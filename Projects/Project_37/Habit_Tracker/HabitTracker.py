import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Travel",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"

}
headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Km did you Travel Today? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)


