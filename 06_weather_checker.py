import requests

city = input("Enter city name: ")
url = f"https://wttr.in/{city}?format=3"
response = requests.get(url)
print("Weather:", response.text)
