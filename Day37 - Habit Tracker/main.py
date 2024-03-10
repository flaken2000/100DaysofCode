import requests
from datetime import date, timedelta

pixela_endpoint = "https://pixe.la/v1/users"
pixela_username = ""
pixela_token = ""

# Post a Pixel
graph_id = "graph01"
pixel_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}"
date_to_post = date.today()  # - timedelta(days=1)
date_to_post = date_to_post.strftime("%Y%m%d")

pixel_params = {
    "date": date_to_post,
    "quantity": input("How many minutes did you code today?: "),
}

headers = {
    "X-USER-TOKEN": pixela_token
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
response.raise_for_status()
print(response.text)

# Below was used to create the user
# user_params = {
#     "token": "",
#     "username": "",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

# Create a Graph Definition
# graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"
# graph_params = {
#     "id": "graph01",
#     "name": "100 Days of Code Graph",
#     "unit": "Minutes",
#     "type": "int",
#     "color": "ajisai"
# }
#
# headers = {
#     "X-USER-TOKEN": pixela_token
# }
#
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# response.raise_for_status()
# print(response.text)
