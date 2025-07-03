import unittest
from agrim_system.python_ai.irrigation_models import (
    SmartIrrigationRLAgent,
    water_requirement_prediction,
    flooding_risk_prediction,
    irrigation_rainfall_overlap_optimization,
    et_water_loss_estimator,
    irrigation_efficiency_predictor
)
import numpy as np

class TestIrrigationModels(unittest.TestCase):
    def test_water_requirement_prediction(self):
        result = water_requirement_prediction(20, {'temperature': 35}, 'Wheat')
        self.assertIn("Predicted water requirement", result)

    def test_flooding_risk_prediction(self):
        result = flooding_risk_prediction(120, 1)
        self.assertEqual(result, "High flooding risk")

    def test_irrigation_rainfall_overlap_optimization(self):
        schedule = [("08:00", 10), ("18:00", 10)]
        rainfall = {"08:00": 5, "18:00": 0}
        optimized = irrigation_rainfall_overlap_optimization(schedule, rainfall)
        self.assertEqual(optimized[0][1], 0)
        self.assertEqual(optimized[1][1], 10)

    def test_et_water_loss_estimator(self):
        result = et_water_loss_estimator(5, 10)
        self.assertIn("Estimated water loss", result)

    def test_irrigation_efficiency_predictor(self):
        data = {'water_used': 100, 'crop_yield': 150}
        result = irrigation_efficiency_predictor(data)
        self.assertIn("High irrigation efficiency", result)

if __name__ == '__main__':
    unittest.main()
