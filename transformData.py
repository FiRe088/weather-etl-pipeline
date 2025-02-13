import json
from extractData import fetch_weather_data
import pandas as pd

def transform_data(data):
    if 'hourly' not in data:
        print('Invalid data format')
        return None

    hourly_data = data['hourly']
    transformed_data = []

    for i in range(len(hourly_data['time'])):
        entry = {
            'time': hourly_data['time'][i],
            'temperature': hourly_data['temperature_2m'][i],
            'rain': hourly_data['rain'][i]
        }
        transformed_data.append(entry)

    return transformed_data

if __name__ == '__main__':
    weather_data = fetch_weather_data()

    if weather_data:
        cleaned_data = transform_data(weather_data)
        print(json.dumps(cleaned_data, indent=4))
    else:
        print('No data to transform')

