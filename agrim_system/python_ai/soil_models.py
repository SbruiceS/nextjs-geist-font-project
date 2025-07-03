"""
Soil analysis AI models for AgriML system.
Includes:
- Soil type classification (loamy, sandy, clay)
- Soil fertility prediction
- Soil nutrient deficiency detection
- Soil moisture estimation (image + sensor fusion)
- Salinity stress detection
- Soil erosion prediction
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

def build_soil_type_classification_model(input_shape=(64, 64, 3), num_classes=3):
    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D(2,2),
        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

def soil_fertility_prediction(features):
    """
    Predict soil fertility score based on sensor features.
    """
    # Dummy linear model
    weights = np.array([0.3, 0.4, 0.3])
    score = np.dot(features, weights)
    return f"Soil fertility score: {score:.2f}"

def soil_nutrient_deficiency_detection(nutrient_levels):
    """
    Detect nutrient deficiencies from soil nutrient levels.
    """
    deficiencies = []
    if nutrient_levels.get('nitrogen', 0) < 10:
        deficiencies.append("Nitrogen deficiency")
    if nutrient_levels.get('phosphorus', 0) < 5:
        deficiencies.append("Phosphorus deficiency")
    if nutrient_levels.get('potassium', 0) < 5:
        deficiencies.append("Potassium deficiency")
    if deficiencies:
        return ", ".join(deficiencies)
    return "No nutrient deficiencies detected"

def soil_moisture_estimation(image_data, sensor_data):
    """
    Estimate soil moisture by fusing image and sensor data.
    """
    # Dummy fusion: average of sensor moisture and image-based estimate
    image_moisture_estimate = 0.5  # Placeholder
    sensor_moisture = sensor_data.get('moisture', 0.5)
    estimated_moisture = (image_moisture_estimate + sensor_moisture) / 2
    return f"Estimated soil moisture: {estimated_moisture:.2f}"

def salinity_stress_detection(salinity_level):
    """
    Detect salinity stress based on salinity level.
    """
    if salinity_level > 4:
        return "High salinity stress detected"
    elif salinity_level > 2:
        return "Moderate salinity stress"
    else:
        return "No salinity stress"

def soil_erosion_prediction(terrain_data):
    """
    Predict soil erosion risk based on terrain and rainfall data.
    """
    slope = terrain_data.get('slope', 0)
    rainfall = terrain_data.get('rainfall', 0)
    risk = slope * rainfall
    if risk > 50:
        return "High soil erosion risk"
    elif risk > 20:
        return "Moderate soil erosion risk"
    else:
        return "Low soil erosion risk"
