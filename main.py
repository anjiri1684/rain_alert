import requests
from twilio.rest import Client


OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "d876c0cd4ca08ddaeb8024d41ff84222"
account_sid = "ACdaeb35a45b9a54a57a1ecc89056d33b4"
auth_token = "51c51aaaafe4f04f35546ad29b0dad19"

weather_params = {
    "lat": -0.710000,
    "lon": 36.294319,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today.Remember to carry an umbrella☔☔",
        from_='+14352646818',
        to='+254705423996'
    )

    print(message.status)