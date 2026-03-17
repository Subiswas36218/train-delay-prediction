# 🚆 Train Delay Prediction using Machine Learning

## 🌍 Live Demo
👉 https://train-delay-prediction-subhankar.streamlit.app

## 📂 GitHub Repository
👉 https://github.com/Subiswas36218/train-delay-prediction

---

## 📌 Overview

This project predicts train arrival delays using machine learning based on operational and environmental factors such as departure delay, weather, distance, train type, and station congestion.

It demonstrates a **complete end-to-end ML system** including data processing, model training, API development, UI dashboard, and cloud deployment.

---

## 🧠 Features

- 📊 Exploratory Data Analysis (EDA)
- ⚙️ Data preprocessing pipeline
- 🤖 Random Forest regression model
- 📈 Model evaluation (MAE, R² Score)
- 🌐 REST API using Flask
- 🎛️ Interactive dashboard using Streamlit
- 🐳 Docker containerization
- ☁️ AWS deployment ready
- 🔁 CI/CD with GitHub Actions

---

## 🛠️ Tech Stack

- Python 3.12
- Pandas, NumPy
- Scikit-learn
- Flask
- Streamlit
- Docker
- GitHub Actions

---

## 📊 Machine Learning Pipeline

1. Data collection (CSV dataset)
2. Data preprocessing (encoding + feature selection)
3. Model training (Random Forest)
4. Model evaluation
5. Model serialization (joblib)
6. Deployment via API & UI

---

## 🚀 How to Run Locally

### 1. Clone the repository:
```bash
git clone https://github.com/Subiswas36218/train-delay-prediction.git
cd train-delay-prediction

2. Create virtual environment:
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies:
pip install -r requirements.txt

4. Train the model:
python src/train_model.py

5. Run Flask API:
python src/api.py

6. Run Streamlit Dashboard:
streamlit run src/app.py

🌐 API Usage

Endpoint:
POST /predict

Example Request:
{
  "departure_delay": 5,
  "distance_km": 200,
  "weather": "clear",
  "train_type": "regional",
  "congestion": "low"
}

Response:
{
  "predicted_delay": 4.32
}

🐳 Docker Usage:
docker build -t train-delay-app .
docker run -p 5000:5000 train-delay-app

☁️ Deployment:
	•	Streamlit Cloud (Frontend UI)
	•	AWS EC2 (Backend API)
	•	Docker container for portability
	•	GitHub Actions for CI/CD

📈 Results:
	•	Mean Absolute Error (MAE): ~X minutes
	•	R² Score: ~X

🔮 Future Improvements:
	•	Real-time railway data integration
	•	Deep learning models (LSTM)
	•	Database integration (PostgreSQL)
	•	Kubernetes deployment
