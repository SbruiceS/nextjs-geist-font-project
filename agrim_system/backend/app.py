from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from models.irrigation_model import predict_irrigation

app = FastAPI()

# CORS setup for frontend-backend interaction
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://heroic-taiyaki-623aeb.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IrrigationInput(BaseModel):
    soil_moisture: float = Field(..., ge=0, le=100, description="Soil moisture percentage")
    temperature: float = Field(..., description="Temperature in Celsius")
    humidity: float = Field(..., ge=0, le=100, description="Humidity percentage")
    crop_type: str = Field(..., description="Crop type")
    rainfall: Optional[float] = Field(0.0, description="Recent or predicted rainfall in mm")

class IrrigationOutput(BaseModel):
    recommended_volume: float
    irrigation_timing: str
    irrigation_duration_hours: float
    irrigation_status: str
    status_color: str

@app.post("/api/irrigation_advisor", response_model=IrrigationOutput)
async def irrigation_advisor(input_data: IrrigationInput):
    try:
        result = predict_irrigation(
            soil_moisture=input_data.soil_moisture,
            temperature=input_data.temperature,
            humidity=input_data.humidity,
            crop_type=input_data.crop_type,
            rainfall=input_data.rainfall
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
