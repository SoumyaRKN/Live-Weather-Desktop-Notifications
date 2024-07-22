import os
import requests
import notify2
from dotenv import load_dotenv

def send_notification(name, heading, message):
    notify2.init(name)
    notification = notify2.Notification(heading, message)
    notification.show()

def get_weather_report(location='Chandbali'):
    url = f'http://api.weatherapi.com/v1/forecast.json?key={os.getenv('WEATHER_API_KEY')}&q={location}'
    response = requests.get(url)
    data = response.json()

    city = data['location']['name']
    region = data['location']['region']
    country = data['location']['country']
    condition =   data['current']['condition']['text']
    temperature = data['current']['temp_c']
    wind_speed =  data['current']['wind_kph']
    pressure =  data['current']['pressure_mb']
    humidity =  data['current']['humidity']
    
    return city, region, country, condition, temperature, wind_speed, pressure, humidity


if __name__ == '__main__':
    load_dotenv()

    city, region, country, condition, temperature, wind_speed, pressure, humidity = get_weather_report()

    heading = f'{condition} {city}, {region} - {country}.'
    message = f'Temperature is {temperature} °C, wind speed {wind_speed} KPH air pressure {pressure} MB and humidity is {humidity}'

    send_notification('Weather Update', heading, message)
    