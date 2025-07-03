"""
This module contains multiple Keras AI models for various agricultural analytics tasks,
including crop disease detection, pest detection, irrigation optimization, and weather prediction.
"""

import tensorflow as tf
from tensorflow.keras import layers, models

def build_crop_disease_model(input_shape=(224, 224, 3), num_classes=10):
    base_model = tf.keras.applications.MobileNetV2(input_shape=input_shape,
                                                   include_top=False,
                                                   weights='imagenet')
    base_model.trainable = False
    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

def build_pest_detection_model(input_shape=(224, 224, 3), num_classes=5):
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

def build_irrigation_optimization_model(input_shape=(10,)):
    model = models.Sequential([
        layers.Dense(64, activation='relu', input_shape=input_shape),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='linear')  # Predict irrigation amount
    ])
    return model

def build_weather_prediction_model(input_shape=(24, 5)):
    model = models.Sequential([
        layers.LSTM(64, return_sequences=True, input_shape=input_shape),
        layers.LSTM(32),
        layers.Dense(16, activation='relu'),
        layers.Dense(1)  # Predict temperature or rainfall
    ])
    return model
