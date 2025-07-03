import unittest
import numpy as np
from agrim_system.python_ai.weather_models import (
    build_lstm_weather_forecast_model,
    prophet_forecast,
    rainfall_prediction_classification,
    rainfall_prediction_regression,
    drought_forecasting,
    temperature_trend_modeling,
    evapotranspiration_estimation,
    climate_zone_classification
)
import pandas as pd

class TestWeatherModels(unittest.TestCase):
    def test_rainfall_prediction_classification(self):
        features = {'humidity': 80}
        result = rainfall_prediction_classification(features)
        self.assertEqual(result, "Rain")

    def test_rainfall_prediction_regression(self):
        features = {'humidity': 80, 'temperature': 30}
        result = rainfall_prediction_regression(features)
        self.assertIn("Predicted rainfall", result)

    def test_drought_forecasting(self):
        sensor_data = {'soil_moisture': [10, 12, 14], 'temperature': [36, 37, 38]}
        result = drought_forecasting(sensor_data)
        self.assertIn("drought risk", result)

    def test_temperature_trend_modeling(self):
        temps = [20, 21, 22, 23, 24]
        result = temperature_trend_modeling(temps)
        self.assertIn("trend", result)

    def test_evapotranspiration_estimation(self):
        weather = {'temperature': 30, 'humidity': 50, 'wind_speed': 3}
        result = evapotranspiration_estimation(weather)
        self.assertIn("Estimated ET", result)

    def test_climate_zone_classification(self):
        result = climate_zone_classification(28, 1200)
        self.assertEqual(result, "Tropical")

if __name__ == '__main__':
    unittest.main()
