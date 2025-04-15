# Waiting Time Prediction API

A Flask API that predicts waiting time ranges for transportation services using machine learning.

## Project Structure
```
project_folder/
├── app.py                # Main Flask application
├── requirements.txt      # Project dependencies
├── README.md            # Project documentation
├── xgb_model_os.pkl     # Trained XGBoost model
├── encoder.pkl          # Fitted OneHotEncoder
└── scaler.pkl          # Fitted StandardScaler
```

## API Documentation

### Base URL
`/` - Health check endpoint
- Method: GET
- Response: "Waiting Time Prediction API is running."

### Prediction Endpoint
`/predict` - Get waiting time prediction
- Method: POST
- Content-Type: application/json

#### Request Structure
```json
{
    "Age": 21,               // Integer: User's age
    "Gender": "male",        // String: "male" or "female"
    "From": "هانوفيل",       // String: Starting location
    "To": "موقف",           // String: Destination
    "Time": "From 6 AM To 9 AM", // String: Time range
    "IsRainy": "yes",        // String: "yes" or "no"
    "IsWeekend": "yes"       // String: "yes" or "no"
}
```

#### Response Structure
```json
{
    "prediction": "0 to 20 minutes" // Possible values: "0 to 20 minutes", "20 to 40 minutes", "40 to 60 minutes", "more than 60 minutes"
}
```

#### Error Response
```json
{
    "error": "error message"
}
```

## Testing

### Using cURL
```bash
curl -X POST \
  http://localhost:5000/predict \
  -H 'Content-Type: application/json' \
  -d '{
    "Age": 21,
    "Gender": "male",
    "From": "هانوفيل",
    "To": "موقف",
    "Time": "From 6 AM To 9 AM",
    "IsRainy": "yes",
    "IsWeekend": "yes"
}'
```

### Using Python
```python
import requests

url = "http://localhost:5000/predict"
data = {
    "Age": 21,
    "Gender": "male",
    "From": "هانوفيل",
    "To": "موقف",
    "Time": "From 6 AM To 9 AM",
    "IsRainy": "yes",
    "IsWeekend": "yes"
}

response = requests.post(url, json=data)
print(response.json())
```

## Deployment Instructions

1. Ensure all files are in the project directory
2. Create a Railway account if you haven't already
3. Install Railway CLI or use Railway Dashboard
4. Deploy using Railway CLI or GitHub integration