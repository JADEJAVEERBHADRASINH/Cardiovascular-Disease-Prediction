"""
Pydantic schemas with data validation and cross-field consistency checks.
"""
from pydantic import BaseModel, Field, model_validator
from typing import List, Optional

class PatientInput(BaseModel):
    age: int = Field(..., ge=18, le=110, description="Patient age in years")
    gender: int = Field(..., ge=1, le=2, description="Biological sex (1=Female, 2=Male)")
    height: float = Field(..., ge=100.0, le=250.0, description="Height in cm")
    weight: float = Field(..., ge=30.0, le=250.0, description="Weight in kg")
    ap_hi: int = Field(..., ge=60, le=260, description="Systolic blood pressure (mmHg)")
    ap_lo: int = Field(..., ge=40, le=180, description="Diastolic blood pressure (mmHg)")
    cholesterol: int = Field(..., ge=1, le=3, description="Cholesterol level (1=Normal, 2=Above, 3=High)")
    gluc: int = Field(..., ge=1, le=3, description="Glucose level (1=Normal, 2=Above, 3=High)")
    smoke: int = Field(..., ge=0, le=1, description="Smoking status (0=No, 1=Yes)")
    alco: int = Field(..., ge=0, le=1, description="Alcohol consumption (0=No, 1=Yes)")
    active: int = Field(..., ge=0, le=1, description="Physical activity (0=No, 1=Yes)")

    @model_validator(mode="after")
    def validate_pressures(self):
        if self.ap_lo >= self.ap_hi:
            raise ValueError("Diastolic pressure (ap_lo) cannot exceed or equal systolic pressure (ap_hi).")
        return self

class FactorDetail(BaseModel):
    name: str
    value: str
    status: str
    impact: str
    color: str

class PredictionOutput(BaseModel):
    prediction: int
    risk_probability: float
    risk_percentage: float
    risk_label: str
    model_used: str
    top_contributing_factors: List[FactorDetail]
