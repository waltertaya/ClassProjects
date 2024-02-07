import requests


endpoint = "http://127.0.0.1:8000/api/"

# print((requests.get(endpoint)).status_code)
get_response = requests.get(endpoint, params={"price_id": 123})
print(get_response.json())
