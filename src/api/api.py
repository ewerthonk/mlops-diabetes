from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from joblib import load
import numpy as np

project_path = Path(__file__).resolve().parents[2]
model_path = project_path / "models" / "model.joblib"

class Patient(BaseModel):
    pregnancies	: int 
    glucose: int 
    blood_pressure: int
    skin_thickness: int 
    insulin: int 
    bmi: float 
    diabetes_pedigree_function: float 
    age: int
    class Config:
        schema_extra = {
            "example": {
                "pregnancies": 1, 
                "glucose": 100, 
                "blood_pressure": 70,
                "skin_thickness": 30,
                "insulin": 50,
                "bmi": 30,
                "diabetes_pedigree_function": 0.5,
                "age": 30
            }
        }

description = (
    """Features:

    pregnancies: Number of times pregnant

    glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test

    blood_pressure: Diastolic blood pressure (mm Hg)

    skin_thickness: Triceps skin fold thickness (mm)

    insulin: 2-Hour serum insulin (mu U/ml)

    bmi: Body mass index (weight in kg/(height in m)^2)

    diabetes_pedigree_function: Diabetes pedigree function

    age: age in years
"""
)

app = FastAPI(
    title="Diabetes Prediction Model API",
    description=description)

@app.on_event("startup")
def load_model():
    global model
    model = load(model_path)

@app.get("/")
def status() -> dict:
    return {"status": "on"}

@app.post('/predict')
def get_patient_to_predict(data: Patient):
    received = data.dict()
    pregnancies	= received["pregnancies"]
    glucose	= received["glucose"]
    blood_pressure = received["blood_pressure"]
    skin_thickness = received["skin_thickness"]
    insulin = received["insulin"]
    bmi = received["bmi"]
    diabetes_pedigree_function = received["diabetes_pedigree_function"] 
    age = received["age"] 
    pred_proba = model.predict_proba(np.array([
        pregnancies,
        glucose, 
        blood_pressure, 
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree_function,
        age
    ]).reshape(1, -1))
    if pred_proba[0][0] > pred_proba[0][1]:
        predicted_class = "does not have diabetes"
        percentage = pred_proba[0][0] 
    else:
        predicted_class = "has diabetes"
        percentage = pred_proba[0][1]
    return (f"The model predicts - with {percentage*100:.2f}% probability - the patient {predicted_class}")
