import requests
from twilio.rest import Client

account_sid = "AC5971167436a8c10156f0341c55d41888"
auth_token = "Token_goes_here"

weather_parameters = {
    "lat": 30.044420,
    "lon": 31,
    "appid": "api_goes_here",
    "units": "metric",
    "exclude": "daily,current"

}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_parameters)
response.raise_for_status()
data = response.json()
weather_hourly = data["hourly"]
# id = weather_hourly[0]['weather'][0]['id']

will_rain = True
weather = []
id = []
for i in range(len(weather_hourly)):
    weather.append(weather_hourly[i]['weather'])
for i in range(len(weather)):
    id.append(weather[i][0]['id'])
id = id[:12]
for i in range(len(id)):
    if id[i] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
# print(id)
    message = client.messages \
                    .create(
                         body="bring an umbrella ☔",
                         from_='+17262248007',
                         to=   "My_Phone_number"
                 )
    print(message.status)
