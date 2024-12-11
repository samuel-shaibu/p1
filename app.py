from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load the trained model (assuming the model has been saved)
model = joblib.load('churn_model.pkl')

@app.post("/predict")
def predict_churn(data: dict):
    # Convert input data into a numpy array (or format it as required)
    input_data = np.array(list(data.values())).reshape(1, -1)
    prediction = model.predict(input_data)
    
    # Return the prediction
    return {"churn_prediction": "Yes" if prediction[0] == 1 else "No"}
