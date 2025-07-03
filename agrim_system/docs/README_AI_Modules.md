# AgriML AI Modules Documentation

This document provides an overview, usage, and testing instructions for the standalone AI modules in the AgriML system.

## Modules Overview

- **crop_disease_detection.py**: AI service for crop disease detection using CNN and KNN models.
- **advanced_crop_models.py**: Advanced crop analysis models including crop type identification, stage detection, segmentation, and field boundary detection.
- **soil_models.py**: Soil analysis models including soil type classification, fertility prediction, nutrient deficiency detection, moisture estimation, salinity stress, and erosion prediction.
- **weather_models.py**: Weather and climate models including hyperlocal forecasting, rainfall prediction, drought forecasting, temperature trend, ET₀ estimation, and climate zone classification.
- **crop_yield_models.py**: Crop yield and growth forecasting models using XGBoost, LSTM, and CNN-LSTM hybrid.
- **irrigation_models.py**: Irrigation and water management models including reinforcement learning-based scheduling, water requirement prediction, flooding risk, irrigation optimization, water loss estimation, and efficiency prediction.

## Usage

Each module is designed to be used independently or integrated into backend services.

### Running Crop Disease Detection Service

```bash
cd agrim_system/python_ai
python crop_disease_detection.py
```

### Testing Models

You can write test scripts to import and call functions from these modules with sample data.

Example:

```python
from advanced_features import soil_nutrient_analysis

sample_data = {'nitrogen': 8, 'phosphorus': 6, 'potassium': 7}
print(soil_nutrient_analysis(sample_data))
```

## Deployment

- Dockerfiles are provided for containerizing each module.
- Kubernetes manifests are available for deploying the system securely and scalably.
- Backend API using FastAPI is implemented for irrigation advisor.

## Extensibility

- Models are modular and can be replaced or extended with custom-trained models.
- Kafka integration enables real-time data streaming and processing.
- AI models can be enhanced with additional data sources and sensors.

## Contact

For further assistance or customization, please contact the development team.
