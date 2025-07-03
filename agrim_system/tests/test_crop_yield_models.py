import unittest
import numpy as np
from agrim_system.python_ai.crop_yield_models import (
    build_lstm_yield_prediction_model,
    build_cnn_lstm_hybrid_model,
    xgboost_yield_prediction,
    crop_growth_forecasting,
    biomass_estimation,
    harvest_readiness_prediction,
    yield_loss_estimation,
    crop_roi_prediction
)

class TestCropYieldModels(unittest.TestCase):
    def test_crop_growth_forecasting(self):
        data = ['seedling', 'vegetative', 'flowering']
        result = crop_growth_forecasting(data)
        self.assertIn("Predicted next growth stage", result)

    def test_biomass_estimation(self):
        features = np.array([1.0, 2.0, 3.0])
        result = biomass_estimation(None, features)
        self.assertIn("Estimated biomass", result)

    def test_harvest_readiness_prediction(self):
        sensor_data = {'moisture': 10, 'color_index': 0.8}
        result = harvest_readiness_prediction(sensor_data)
        self.assertEqual(result, "Harvest ready")

    def test_yield_loss_estimation(self):
        stress_data = {'level': 0.3}
        disease_data = {'severity': 0.4}
        result = yield_loss_estimation(stress_data, disease_data)
        self.assertIn("Estimated yield loss", result)

    def test_crop_roi_prediction(self):
        roi = crop_roi_prediction(10, {'price_per_ton': 100, 'total_cost': 500})
        self.assertIn("Estimated ROI", roi)

if __name__ == '__main__':
    unittest.main()
