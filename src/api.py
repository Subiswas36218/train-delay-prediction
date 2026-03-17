from flask import Flask, request, jsonify
import joblib
import pandas as pd
import logging

# Initialize app
app = Flask(__name__)

# Logging setup
logging.basicConfig(level=logging.INFO)

# Load model safely
try:
    model = joblib.load("models/delay_model.pkl")
    logging.info("Model loaded successfully")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    model = None

# Required input fields
REQUIRED_FIELDS = [
    "departure_delay",
    "distance_km",
    "weather",
    "train_type",
    "congestion"
]

# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "🚆 Train Delay Prediction API Running",
        "endpoints": {
            "/predict": "POST - Predict delay",
            "/health": "GET - Health check"
        }
    })

# Health check
@app.route("/health")
def health():
    if model:
        return jsonify({"status": "OK"})
    else:
        return jsonify({"status": "Model not loaded"}), 500

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    if not model:
        return jsonify({"error": "Model not available"}), 500

    try:
        data = request.get_json()

        # Validate input
        missing_fields = [field for field in REQUIRED_FIELDS if field not in data]
        if missing_fields:
            return jsonify({
                "error": "Missing required fields",
                "missing": missing_fields
            }), 400

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Prediction
        prediction = model.predict(df)[0]

        return jsonify({
            "input": data,
            "predicted_delay": round(float(prediction), 2),
            "unit": "minutes"
        })

    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({
            "error": "Prediction failed",
            "details": str(e)
        }), 500


# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)