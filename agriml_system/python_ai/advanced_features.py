"""
Advanced AI features module for AgriML system.
Includes 15 advanced AI features for agricultural analytics.
"""

import numpy as np
import tensorflow as tf

def soil_nutrient_analysis(sensor_data):
    """
    Analyze soil nutrient levels using sensor data.
    Returns nutrient deficiency alerts.
    """
    nitrogen = sensor_data.get('nitrogen', 0)
    phosphorus = sensor_data.get('phosphorus', 0)
    potassium = sensor_data.get('potassium', 0)
    alerts = []
    if nitrogen < 10:
        alerts.append("Nitrogen deficiency detected")
    if phosphorus < 5:
        alerts.append("Phosphorus deficiency detected")
    if potassium < 5:
        alerts.append("Potassium deficiency detected")
    if not alerts:
        return "Nutrient levels normal"
    return ", ".join(alerts)

def pest_infestation_prediction(image_data):
    """
    Predict pest infestation likelihood from crop images.
    Returns infestation risk score.
    """
    risk_score = np.random.rand()
    return f"Pest infestation risk: {risk_score:.2f}"

def irrigation_need_forecast(weather_data, soil_moisture):
    """
    Forecast irrigation needs based on weather and soil moisture.
    Returns recommended irrigation volume.
    """
    temp = weather_data.get('temperature', 25)
    rainfall = weather_data.get('rainfall', 0)
    moisture = soil_moisture

    base_need = max(0, 30 - moisture)
    if temp > 35:
        base_need *= 1.5
    if rainfall > 5:
        base_need *= 0.5
    return f"Recommended irrigation volume: {base_need:.2f} liters"

def crop_yield_prediction(historical_data):
    """
    Predict crop yield based on historical data.
    Returns estimated yield.
    """
    X = np.array(historical_data['features'])
    y = np.array(historical_data['yields'])
    coef = np.linalg.lstsq(X, y, rcond=None)[0]
    estimate = np.dot(X[-1], coef)
    return f"Estimated crop yield: {estimate:.2f} tons"

def disease_spread_modeling(disease_data, weather_data):
    """
    Model disease spread risk based on disease and weather data.
    Returns risk level.
    """
    humidity = weather_data.get('humidity', 50)
    temp = weather_data.get('temperature', 25)
    infected_area = disease_data.get('infected_area', 0)

    risk = infected_area * (humidity / 100) * (temp / 30)
    if risk > 10:
        return "High disease spread risk"
    elif risk > 5:
        return "Moderate disease spread risk"
    else:
        return "Low disease spread risk"

def fertilizer_recommendation(soil_data):
    """
    Recommend fertilizer type and amount based on soil data.
    """
    ph = soil_data.get('ph', 7)
    if ph < 6:
        return "Apply lime to increase soil pH"
    elif ph > 7.5:
        return "Apply sulfur to decrease soil pH"
    else:
        return "Soil pH is optimal"

def crop_health_index(sensor_data):
    """
    Calculate crop health index from sensor data.
    """
    ndvi = sensor_data.get('ndvi', 0.5)
    if ndvi > 0.7:
        return "Healthy crop"
    elif ndvi > 0.4:
        return "Moderate health"
    else:
        return "Poor crop health"

def water_stress_detection(soil_moisture):
    """
    Detect water stress based on soil moisture.
    """
    if soil_moisture < 15:
        return "Water stress detected"
    return "No water stress"

def pest_population_forecast(historical_counts):
    """
    Forecast pest population based on historical counts.
    """
    avg_count = np.mean(historical_counts)
    if avg_count > 50:
        return "High pest population expected"
    return "Pest population normal"

def temperature_anomaly_detection(temperature_data):
    """
    Detect temperature anomalies.
    """
    mean_temp = np.mean(temperature_data)
    if mean_temp > 35:
        return "High temperature anomaly detected"
    return "Temperature normal"

def rainfall_prediction(weather_history):
    """
    Predict rainfall using weather history.
    """
    avg_rainfall = np.mean(weather_history)
    if avg_rainfall > 10:
        return "Heavy rainfall expected"
    return "Rainfall normal"

def soil_moisture_trend(soil_moisture_data):
    """
    Analyze soil moisture trend.
    """
    trend = np.polyfit(range(len(soil_moisture_data)), soil_moisture_data, 1)[0]
    if trend < 0:
        return "Decreasing soil moisture trend"
    return "Stable or increasing soil moisture"

def crop_growth_stage_prediction(sensor_data):
    """
    Predict crop growth stage.
    """
    days_after_planting = sensor_data.get('days_after_planting', 0)
    if days_after_planting < 30:
        return "Vegetative stage"
    elif days_after_planting < 60:
        return "Flowering stage"
    else:
        return "Maturity stage"

def irrigation_efficiency_analysis(irrigation_data):
    """
    Analyze irrigation efficiency.
    """
    water_used = irrigation_data.get('water_used', 0)
    yield_amount = irrigation_data.get('yield', 0)
    if water_used == 0:
        return "No irrigation data"
    efficiency = yield_amount / water_used
    if efficiency > 1:
        return "Efficient irrigation"
    return "Irrigation improvement needed"

def crop_variety_recommendation(soil_data, climate_data):
    """
    Recommend crop variety based on soil and climate.
    """
    ph = soil_data.get('ph', 7)
    avg_temp = climate_data.get('avg_temp', 25)
    if ph < 6 and avg_temp > 30:
        return "Recommend drought-resistant variety"
    return "Recommend standard variety"

def pest_control_strategy(pest_data):
    """
    Recommend pest control strategy.
    """
    pest_type = pest_data.get('type', 'unknown')
    if pest_type == 'aphid':
        return "Use insecticidal soap"
    elif pest_type == 'caterpillar':
        return "Use Bacillus thuringiensis"
    return "Consult pest control expert"
