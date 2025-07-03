"""
Crop yield and growth forecasting models for AgriML system.
Includes:
- Crop yield prediction (XGBoost, LSTM, CNN-LSTM hybrid)
- Crop growth forecasting
- Biomass estimation (remote sensing + ML)
- Harvest readiness prediction
- Yield loss estimation due to stress or disease
- Crop ROI prediction model
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import xgboost as xgb

def build_lstm_yield_prediction_model(input_shape=(30, 10)):
    model = models.Sequential([
        layers.LSTM(64, return_sequences=True, input_shape=input_shape),
        layers.LSTM(32),
        layers.Dense(16, activation='relu'),
        layers.Dense(1)  # Predict yield
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def build_cnn_lstm_hybrid_model(image_shape=(64, 64, 3), time_steps=10, feature_dim=5):
    # CNN for image feature extraction
    cnn_input = layers.Input(shape=image_shape)
    x = layers.Conv2D(32, (3,3), activation='relu')(cnn_input)
    x = layers.MaxPooling2D(2,2)(x)
    x = layers.Conv2D(64, (3,3), activation='relu')(x)
    x = layers.MaxPooling2D(2,2)(x)
    x = layers.Flatten()(x)
    cnn_model = models.Model(inputs=cnn_input, outputs=x)

    # LSTM for time series
    lstm_input = layers.Input(shape=(time_steps, feature_dim))
    y = layers.LSTM(64)(lstm_input)

    # Combine CNN and LSTM features
    combined = layers.concatenate([cnn_model.output, y])
    z = layers.Dense(64, activation='relu')(combined)
    z = layers.Dense(1)(z)

    model = models.Model(inputs=[cnn_model.input, lstm_input], outputs=z)
    model.compile(optimizer='adam', loss='mse')
    return model

def xgboost_yield_prediction(X_train, y_train, X_test):
    model = xgb.XGBRegressor(objective='reg:squarederror')
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    return preds

def crop_growth_forecasting(time_series_data):
    """
    Forecast crop growth stage progression.
    """
    # Dummy logic: predict next stage based on current stage
    current_stage = time_series_data[-1]
    stages = ['seedling', 'vegetative', 'flowering', 'harvest-ready']
    try:
        idx = stages.index(current_stage)
        next_stage = stages[min(idx+1, len(stages)-1)]
    except ValueError:
        next_stage = 'unknown'
    return f"Predicted next growth stage: {next_stage}"

def biomass_estimation(remote_sensing_data, ml_features):
    """
    Estimate biomass using remote sensing and ML features.
    """
    # Dummy linear model
    weights = np.array([0.4, 0.3, 0.3])
    score = np.dot(ml_features, weights)
    return f"Estimated biomass: {score:.2f} tons/ha"

def harvest_readiness_prediction(sensor_data):
    """
    Predict harvest readiness based on sensor data.
    """
    moisture = sensor_data.get('moisture', 0)
    color_index = sensor_data.get('color_index', 0)
    if moisture < 15 and color_index > 0.7:
        return "Harvest ready"
    return "Not ready for harvest"

def yield_loss_estimation(stress_data, disease_data):
    """
    Estimate yield loss due to stress or disease.
    """
    stress_level = stress_data.get('level', 0)
    disease_severity = disease_data.get('severity', 0)
    loss = stress_level * 0.5 + disease_severity * 0.5
    return f"Estimated yield loss: {loss*100:.1f}%"

def crop_roi_prediction(yield_estimate, cost_data):
    """
    Predict return on investment for crop.
    """
    revenue = yield_estimate * cost_data.get('price_per_ton', 100)
    cost = cost_data.get('total_cost', 1000)
    roi = (revenue - cost) / cost
    return f"Estimated ROI: {roi*100:.1f}%"
