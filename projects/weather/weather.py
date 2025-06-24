import requests

api_key = "your_openweather_api_key"
city = input("Enter a city: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()

if data["cod"] != "404":
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"The temperature in {city} is {temp}°C with {desc}.")
else:
    print("City not found.")