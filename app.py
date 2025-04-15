#!/usr/bin/env python
# coding: utf-8

# # project_folder/

# ├── app.p
# 
# ├── requirements.txt
# 
# ├── README.md
# 
# ├── xgb_model_os.pkl
# 
# ├── encoder.pkl
# 
# ├── scaler.pkler.pkl

# In[ ]:


from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
import os 

# Initialize the Flask application
app = Flask(__name__)

# Load the saved model and preprocessors
model = joblib.load('xgb_model_os.pkl')
encoder = joblib.load('encoder.pkl')
scaler = joblib.load('scaler.pkl')

# Define the feature columns as used in training
categorical_cols = ["Gender", "From", "To", "Time", "IsRainy", "IsWeekend"]
numerical_cols = ["Age"]

# Define the mapping from predicted labels to waiting time ranges
label_to_range = {
    0: "0 to 20 minutes",
    1: "20 to 40 minutes",
    2: "40 to 60 minutes",
    3: "more than 60 minutes"
}

# Define the required fields for input data
required_fields = numerical_cols + categorical_cols

# Home endpoint to check if the API is running
@app.route('/')
def home():
    return "Waiting Time Prediction API is running."

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Check for missing fields
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({'error': f"Missing fields: {', '.join(missing_fields)}"}), 400

        # Convert the input data into a DataFrame
        input_df = pd.DataFrame([data])

        # Separate numerical and categorical features
        X_num = input_df[numerical_cols]
        X_cat = input_df[categorical_cols]

        # Preprocess the input data
        # Scale numerical features
        X_num_scaled = scaler.transform(X_num)
        # Encode categorical features
        X_cat_encoded = encoder.transform(X_cat)
        # Combine the processed features
        X_processed = np.hstack((X_num_scaled, X_cat_encoded))

        # Make the prediction
        prediction = model.predict(X_processed)[0]

        # Map the predicted label to the waiting time range
        waiting_time_range = label_to_range[prediction]

        # Return the prediction as a JSON response
        return jsonify({'prediction': waiting_time_range})

    except Exception as e:
        # Return an error message if something goes wrong
        return jsonify({'error': str(e)}), 400

# Run the Flask application
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
