from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

#Load the pre-trained churn prediction model
model = joblib.load('churn_model.pkl')

@app.route("/")
def home():
    return "Welcome to the Customer Churn Prediction API!"

@app.route("/predict", methods=["POST"])
def predict():
    #Get input data from the request
    input_data = request.get_json()

    #convert input to the required format(ensure it matches the model's training data format)
    try:
        features = np.array(list(input_data.values())).reshape(-1,1)
        prediction = model.predict(features)
        result = {"churn_prediction": "Yes" if prediction[0] == 1 else "No"}
        return jsonify
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
if __name__ == "__main__":
    app.run(debug=True)
    