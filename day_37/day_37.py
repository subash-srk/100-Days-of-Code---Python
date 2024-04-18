# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# print(today.strftime("%Y%m%d"))

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.post(url=delete_endpoint, headers=headers)
print(response.text)
