from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import joblib
import numpy as np

# Load the trained fraud detection model
model_path = r"C:\GITHUB\Fraud detection\archive\fraud_detection_rf_model.pkl"
model = joblib.load(model_path)

# Initialize FastAPI app
app = FastAPI()

# Define request model with Pydantic v2 syntax
class FraudRequest(BaseModel):
    features: List[float] = Field(..., min_length=30, max_length=30)  # Enforce 30 features

# Define API endpoint
@app.post("/predict")
def predict_fraud(data: FraudRequest):
    features = np.array(data.features).reshape(1, -1)

    # Check if input has exactly 30 features
    if features.shape[1] != 30:
        raise HTTPException(status_code=400, detail="Invalid input: Expected 30 features.")

    prediction = model.predict(features)[0]
    return {"fraud_prediction": int(prediction)}

# Run with: uvicorn app:app --reload
