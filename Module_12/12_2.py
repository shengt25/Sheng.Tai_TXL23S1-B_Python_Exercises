import requests

key = "73f5ed8d4588e986fc942b1b3414e461"

# Enter city name
city_name = input("Enter city/municipality name: ")

# Get weather data
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={key}"
response = requests.get(url)

# Check if response is valid
if response.status_code != 200:
    try:
        print("Error: " + response.json()["message"])
    except:
        print("Error retrieving data")
else:
    # Decode weather data
    weather_desc = response.json()["weather"][0]["description"]
    degree_kelvin = float(response.json()["main"]["temp"])
    degree_celsius = degree_kelvin - 273.15

    # Print weather data
    print("\n")
    print(f"Current weather in {city_name}:")
    print(f"Weather description: {weather_desc}")
    print(f"Temperature: {degree_celsius} C")
