import streamlit as st
import pandas as pd
import joblib
import os

st.title("🚆 Train Delay Prediction")

# ✅ Robust model loading (works locally + cloud)
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "delay_model.pkl")
model = joblib.load(model_path)

# Inputs
departure_delay = st.slider("Departure Delay (minutes)", 0, 60, 5)
distance = st.slider("Distance (km)", 50, 1000, 200)
weather = st.selectbox("Weather", ["clear", "rain", "storm", "cloudy"])
train_type = st.selectbox("Train Type", ["regional", "intercity", "highspeed"])
congestion = st.selectbox("Congestion", ["low", "medium", "high"])

# Prediction
if st.button("Predict Delay"):
    data = pd.DataFrame({
        "departure_delay": [departure_delay],
        "distance_km": [distance],
        "weather": [weather],
        "train_type": [train_type],
        "congestion": [congestion]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Arrival Delay: {prediction[0]:.2f} minutes")