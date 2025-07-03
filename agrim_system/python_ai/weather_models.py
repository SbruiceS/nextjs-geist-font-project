"""
Advanced weather and climate models for AgriML system.
Includes:
- Hyperlocal weather forecasting (LSTM, Prophet)
- Rainfall prediction (classification + regression)
- Drought forecasting (multi-sensor time series)
- Temperature trend modeling
- Evapotranspiration (ET₀) estimation model
- Climate zone classification for crops
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from prophet import Prophet
import pandas as pd

def build_lstm_weather_forecast_model(input_shape=(24, 5)):
    model = models.Sequential([
        layers.LSTM(64, return_sequences=True, input_shape=input_shape),
        layers.LSTM(32),
        layers.Dense(16, activation='relu'),
        layers.Dense(1)  # Predict temperature or rainfall
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def prophet_forecast(time_series_df):
    """
    Use Prophet for time series forecasting.
    time_series_df: pandas DataFrame with columns ['ds', 'y']
    Returns forecast DataFrame.
    """
    model = Prophet()
    model.fit(time_series_df)
    future = model.make_future_dataframe(periods=24, freq='H')
    forecast = model.predict(future)
    return forecast

def rainfall_prediction_classification(features):
    """
    Classify rainfall occurrence (yes/no) based on features.
    """
    # Dummy classifier: threshold on humidity
    humidity = features.get('humidity', 0)
    return "Rain" if humidity > 70 else "No Rain"

def rainfall_prediction_regression(features):
    """
    Predict rainfall amount based on features.
    """
    # Dummy regression: linear function of humidity and temp
    humidity = features.get('humidity', 0)
    temp = features.get('temperature', 25)
    rainfall = 0.1 * humidity + 0.05 * temp
    return f"Predicted rainfall: {rainfall:.2f} mm"

def drought_forecasting(sensor_time_series):
    """
    Forecast drought risk from multi-sensor time series data.
    """
    # Dummy logic: low soil moisture and high temp indicate drought
    soil_moisture = np.mean(sensor_time_series.get('soil_moisture', [0]))
    temperature = np.mean(sensor_time_series.get('temperature', [25]))
    if soil_moisture < 15 and temperature > 35:
        return "High drought risk"
    elif soil_moisture < 20:
        return "Moderate drought risk"
    else:
        return "Low drought risk"

def temperature_trend_modeling(temperature_data):
    """
    Model temperature trend using linear regression.
    """
    x = np.arange(len(temperature_data))
    coef = np.polyfit(x, temperature_data, 1)[0]
    if coef > 0:
        return "Increasing temperature trend"
    elif coef < 0:
        return "Decreasing temperature trend"
    else:
        return "Stable temperature"

def evapotranspiration_estimation(weather_data):
    """
    Estimate reference evapotranspiration (ET₀) using weather data.
    """
    temp = weather_data.get('temperature', 25)
    humidity = weather_data.get('humidity', 50)
    wind_speed = weather_data.get('wind_speed', 2)
    et0 = 0.0023 * (temp + 17.8) * (humidity / 100) * wind_speed
    return f"Estimated ET₀: {et0:.2f} mm/day"

def climate_zone_classification(temperature, rainfall):
    """
    Classify climate zone for crops based on temperature and rainfall.
    """
    if temperature > 25 and rainfall > 1000:
        return "Tropical"
    elif temperature > 15 and rainfall > 500:
        return "Subtropical"
    elif temperature > 5:
        return "Temperate"
    else:
        return "Cold"
