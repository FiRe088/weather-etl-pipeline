import pandas as pd
from sqlalchemy import create_engine
from transformData import transform_data
from extractData import fetch_weather_data

# Database connection details
DB_USER = 'postgres'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'weather_db'

# Create connection
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

def check_for_missing_values(df):
    missing_data = df[df.isnull().any(axis=1)]
    print('Rows with missing data: ',missing_data)

def load_data_to_db(data):
    if data:
        df = pd.DataFrame(data)  # Convert dictionary to DataFrame
        df['temperature'] = df['temperature'].fillna(0)
        df['rain'] = df['rain'].fillna(0)

        df.head()

        df.to_sql('hourly_forecast', con=engine, schema='weather_data', if_exists='append', index=False)
        print('Data successfully loaded into database.')

if __name__ == '__main__':
    weather_data = fetch_weather_data()

    if weather_data:
        cleaned_data = transform_data(weather_data)
        load_data_to_db(cleaned_data)
    else:
        print('Data not loaded')