import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
if response.status_code != 200:
    print("Error: " + response.json()["message"])
else:
    print(response.json()["value"])
