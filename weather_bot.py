import requests
import time

TOKEN = 'TOKEN VAL'
OPEN_METEO_API = 'https://api.open-meteo.com/v1/forecast'


LATITUDE = 55.7558
LONGITUDE = 37.6173

CHAT_ID = 111 

def get_weather():
    
    params = {
        'latitude': LATITUDE,
        'longitude': LONGITUDE,
        'current': 'temperature_2m,wind_speed_10m',
        'hourly': 'temperature_2m,relative_humidity_2m,wind_speed_10m'
    }
    response = requests.get(OPEN_METEO_API, params=params)
    data = response.json()
    current_weather = data['current']
    temperature = current_weather['temperature_2m']
    wind_speed = current_weather['wind_speed_10m']
    hourly_weather = data['hourly']
    hourly_temperature = hourly_weather['temperature_2m'][0]
    hourly_humidity = hourly_weather['relative_humidity_2m'][0]
    hourly_wind_speed = hourly_weather['wind_speed_10m'][0]
    return f'Current weather in Moscow:\nTemperature: {temperature}°C\nWind speed: {wind_speed} m/s\nHourly forecast:\nTemperature: {hourly_temperature}°C\nHumidity: {hourly_humidity}%\nWind speed: {hourly_wind_speed} m/s'

def send_message(text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': CHAT_ID,
        'text': text
    }
    response = requests.post(url, json=params)
    return response.json()

while True:
    weather_text = get_weather()
    send_message(weather_text)
    time.sleep(60)
