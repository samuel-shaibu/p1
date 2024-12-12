from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load the trained model (assuming the model has been saved)
model = joblib.load('churn_model.pkl')

class CustomerData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.post("/predict")
def predict(data: CustomerData):
    #Convert input data to DataFrame
    df = pd.DataFrame([data.dict()])
    #Generate prediction
    prediction = model.predict(df)
    return {"churn": bool(prediction[0])}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Churn Analysis API!"}
