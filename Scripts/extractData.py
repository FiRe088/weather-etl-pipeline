import requests
import json

URL = 'https://api.open-meteo.com/v1/forecast?latitude=51.8985&longitude=8.4756&hourly=temperature_2m,rain&timezone=Europe%2FLondon&past_days=92&forecast_days=16'

def fetch_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error fetching data')
        return None

if __name__ == '__main__':
    weather_data = fetch_weather_data()
    print(json.dumps(weather_data, indent=4))
