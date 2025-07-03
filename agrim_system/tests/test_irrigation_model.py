import unittest
from backend.models.irrigation_model import predict_irrigation

class TestIrrigationModel(unittest.TestCase):
    def test_predict_irrigation_dry(self):
        result = predict_irrigation(soil_moisture=20, temperature=35, humidity=40, crop_type="Wheat", rainfall=0)
        self.assertEqual(result['irrigation_status'], "Dry")
        self.assertGreater(result['recommended_volume'], 20)

    def test_predict_irrigation_wet(self):
        result = predict_irrigation(soil_moisture=70, temperature=25, humidity=60, crop_type="Rice", rainfall=15)
        self.assertEqual(result['irrigation_status'], "Wet")
        self.assertLess(result['recommended_volume'], 20)

    def test_invalid_crop_type(self):
        result = predict_irrigation(soil_moisture=50, temperature=25, humidity=50, crop_type="Unknown", rainfall=0)
        self.assertIn('recommended_volume', result)

if __name__ == '__main__':
    unittest.main()
