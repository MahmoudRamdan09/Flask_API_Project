---

# 🚏 Salka API - Prediction Endpoint

This document describes the request structure for the prediction endpoint used in the "Salka" mobile app.

---

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [API Endpoints](#api-endpoints)
  - [Prediction Endpoint](#prediction-endpoint)
- [Request Structure](#request-structure)
- [Example Usage](#example-usage)
- [Project Structure](#project-structure)
- [License](#license)

---

## Features

- **Machine Learning Integration**: Uses a trained ML model for predictions.
- **RESTful API**: Built using Flask to serve predictions via HTTP requests.
- **JSON Input/Output**: Expects JSON input and returns predictions in JSON format.
- **Scalable Deployment**: Ready-to-deploy on platforms like Railway, Heroku, etc.

---

## Technologies Used

- **Flask**: For building the API.
- **scikit-learn**: For preprocessing and loading the trained machine learning model.
- **Python**: Core programming language.
- **Pandas & NumPy**: For data manipulation and preprocessing.

---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MahmoudRamdan01/flask-api-ml.git
   cd flask-api-ml
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure the correct Python version is installed (specified in `runtime.txt`):
   ```
   python-3.10.12
   ```

5. Run the Flask application:
   ```bash
   python app.py
   ```
   The API will be available at `http://127.0.0.1:5000`.

---

## API Endpoints

### Prediction Endpoint

- **Route**: `/predict`
- **Method**: `POST`
- **Description**: Predicts the waiting time based on input features.

---

## Request Structure

### Headers
- `Content-Type: application/json`

### Request Body
The API expects a JSON object with the following structure:

| Field Name  | Type   | Description                                                                                                                                 |
|-------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `Age`       | Number | The age of the individual.                                                                                                                  |
| `Gender`    | String | The gender of the individual. Accepted values: `male`, `female`.                                                                            |
| `From`      | String | The starting location. Example: `"هانوفيل"`.                                                                                                |
| `To`        | String | The destination location. Example: `"موقف"`.                                                                                                |
| `Time`      | String | The time range of the travel. Accepted values: `"From 6 AM To 9 AM"`, `"From 9 AM To 12 PM"`, etc.                                           |
| `IsRainy`   | String | Whether it is rainy during the travel. Accepted values: `yes`, `no`.                                                                         |
| `IsWeekend` | String | Whether it is a weekend. Accepted values: `yes`, `no`.                                                                                      |

---


## 🔗 Endpoint

**URL:**  
`https://web-production-e146.up.railway.app/predict`

**Method:**  
`POST`

**Content-Type:**  
`application/json`

---

## 📥 Request Body

```json
{
  "Age": 21,
  "Gender": "male",
  "From": "هانوفيل",
  "To": "موقف",
  "Time": "From 6 AM To 9 AM",
  "IsRainy": "yes",
  "IsWeekend": "yes"
}
```

### 📝 Parameters Description

| Field       | Type    | Description                                              |
|-------------|---------|----------------------------------------------------------|
| `Age`       | integer | Age of the user                                          |
| `Gender`    | string  | Gender of the user. (`"male"` or `"female"`)            |
| `From`      | string  | Start location in Arabic                                 |
| `To`        | string  | Destination location in Arabic                          |
| `Time`      | string  | Time range. Example: `"From 6 AM To 9 AM"`              |
| `IsRainy`   | string  | `"yes"` if it's raining, `"no"` otherwise               |
| `IsWeekend` | string  | `"yes"` if it's a weekend, `"no"` otherwise             |

---

## 📤 Response

```json
{
  "prediction": "20 to 40 minutes"
}
```

- The predicted trip duration based on the input conditions.

---

## ✅ Example (Using Curl)

```bash
curl -X POST "https://web-production-e146.up.railway.app/predict" \
-H "Content-Type: application/json" \
-d '{"Age": 21, "Gender": "male", "From": "هانوفيل", "To": "موقف", "Time": "From 6 AM To 9 AM", "IsRainy": "yes", "IsWeekend": "yes"}'
```

---




---

## Project Structure

```plaintext
flask-api-ml/
├── app.py                # Main Flask application
├── encoder.pkl           # Pre-trained encoder for categorical features
├── xgb_model_os.pkl      # Trained ML model
├── scaler.pkl            # Pre-trained scaler for numerical features
├── requirements.txt      # Project dependencies
├── Procfile              # Deployment configuration for Railway/Heroku
└── README.md             # Project documentation
```


---

## License

This project is licensed under the Darsh License. See the [LICENSE](LICENSE) file for details.
