import requests
import json

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"Tokyo"}

headers = {
	"X-RapidAPI-Key": "a0f4c5fe20msh106b1c5a292077cp1192d6jsn9534ee36e30a",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
weather = json.loads(response.text)
print(weather["location"]["region"])
print(weather["location"]["localtime"])
print(weather["current"]["temp_c"])