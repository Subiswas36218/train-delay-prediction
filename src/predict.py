import joblib
import pandas as pd

model = joblib.load("models/delay_model.pkl")

sample = pd.DataFrame({
    "departure_delay": [5],
    "distance_km": [200],
    "weather": ["clear"],
    "train_type": ["regional"],
    "congestion": ["low"]
})

prediction = model.predict(sample)

print("Predicted arrival delay:", prediction[0])