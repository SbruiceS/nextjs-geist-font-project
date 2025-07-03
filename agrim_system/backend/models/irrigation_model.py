from typing import Dict

def predict_irrigation(soil_moisture: float, temperature: float, humidity: float, crop_type: str, rainfall: float = 0.0) -> Dict:
    """
    Simple ML model to predict irrigation volume, timing, duration, and status.
    This is a placeholder for a real trained model.
    """
    # Base recommended volume in liters per hectare
    base_volume = 20.0

    # Adjust volume based on soil moisture
    if soil_moisture < 30:
        volume = base_volume * 1.5
    elif soil_moisture < 60:
        volume = base_volume
    else:
        volume = base_volume * 0.5

    # Adjust volume based on recent rainfall
    if rainfall > 10:
        volume *= 0.5

    # Adjust volume based on crop type (example factors)
    crop_factors = {
        "Wheat": 1.0,
        "Tomato": 1.2,
        "Pepper": 1.1,
        "Corn": 1.3,
        "Rice": 1.5
    }
    volume *= crop_factors.get(crop_type, 1.0)

    # Determine irrigation timing suggestion
    if temperature > 30:
        timing = "Morning"
        duration = 2.0
    else:
        timing = "Evening"
        duration = 1.5

    # Determine irrigation status
    if soil_moisture < 30:
        status = "Dry"
        color = "red"
    elif soil_moisture < 60:
        status = "Optimal"
        color = "green"
    else:
        status = "Wet"
        color = "blue"

    return {
        "recommended_volume": round(volume, 2),
        "irrigation_timing": timing,
        "irrigation_duration_hours": duration,
        "irrigation_status": status,
        "status_color": color
    }
