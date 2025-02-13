CREATE SCHEMA weather_data;

CREATE TABLE weather_data.hourly_forecast (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP NOT NULL,
    temperature DECIMAL(5,2) NOT NULL,
    rain DECIMAL(5,2) NOT NULL
);