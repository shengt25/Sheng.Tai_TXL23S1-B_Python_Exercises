import requests


# --------------------------------------------------
# use a simple encryption to prevent bot/web crawler
# --------------------------------------------------
def de(text, s):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                char = chr((ord(char) + s - 65) % 26 + 65)
            else:
                char = chr((ord(char) + s - 97) % 26 + 97)
        result += char
    return result


k = "m5k3mno470lkmk1n998mo3m53j0n319j"
u1 = "qccyb://jyr.xynwfnjcqnavjy.xap/mjcj/2.5/fnjcqna?z="
u2 = "&jyyrm="
# --------------------------------------------------
# use a simple encryption to prevent bot/web crawler
# --------------------------------------------------


# Enter city name
city_name = input("Enter city/municipality name: ")

# Get weather data
url = de(u1, -9) + city_name + de(u2, -9) + de(k, -9)
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
