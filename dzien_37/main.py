from http.client import responses

import requests
import datetime

# ------------------- Create user ------------------------------
USERNAME = "<username>"
TOKEN = "<token>"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
response = requests.post(url=pixela_endpoint,json=user_params)
print(response.text)


# -------------------------- Create graph ------------------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graphs_config = {
    "id" : "testgraph",
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}
response = requests.post(url=graph_endpoint, json=graphs_config, headers=headers)
print(response.text)


# ------------------- Create pixel ------------------------------
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphs_config['id']}"

date = str(datetime.date.today())
today = date.replace("-","")
kilometers = str(input("How many kilometers you ride today?: "))

post_pixel_params = {
    "date" : today,
    "quantity" : kilometers,
}
post_pixel_response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
print(post_pixel_response.text)

# ------------------- Update pixel ------------------------------
date_to_change = input("Enter the pixel date that you want to change to (USE YYYYMMDD FORMAT): ")
update_kilometers = str(input("How many kilometers you ride the day which you want to change?: "))
update_pixel_params = {
    "quantity" : update_kilometers,
}

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphs_config['id']}/{date_to_change}"
response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
print(response.text)

#-------------------- Delete pixel -------------------------------
date_to_change = input("Enter the pixel date that you want to delete to (USE YYYYMMDD FORMAT): ")
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphs_config['id']}/{date_to_change}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)

