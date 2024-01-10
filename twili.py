import requests
import os
from twilio.rest import Client

api_key = "api"
account_sid = "sid"
auth_token = "token"
number = "+12189673063"
client = Client(account_sid, auth_token)

api_url = "https://api.openweathermap.org/data/2.5/forecast"
parametres = {
    "lat": 48.2864702,
    "lon": 25.9376532,
    "appid": api_key,
    "lang": "ua",
    "units": "metric",
    "cnt": 4,
}

respons = requests.get(url=api_url, params=parametres)
respons.raise_for_status()
data = respons.json()
data_weather = respons.json()["list"]
list_of_sky_data = [
    respons.json()["list"][i]["weather"][0]['id']
    for i in range(len(data_weather))
]
print(list_of_sky_data)
will_rain = False
for i in range(len(data_weather)):
  data_sky_id = respons.json()["list"][i]["weather"][0]['id']
  date_time = respons.json()["list"][i]["dt_txt"]
  if data_sky_id < 700:
    will_rain = True

if will_rain:
  message = client.messages.create(
      body="In 12 hours will be a rain, take a umbrella",
      from_=number,
      to="+380961544914")

  print(message.status)
