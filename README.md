# Exam Score Predictor — Machine Learning + Flask + MySQL

A fully functional ML‑integrated web application that predicts student exam scores using academic parameters such as study hours, attendance, and internal assessment marks.  
This project was designed and developed by **Fazin Firoz**.

## 🚀 Project Overview
The application uses a **Random Forest Regression model** integrated into a **Flask backend**, with a **MySQL database** for storing student records and prediction logs.  
Interactive visualizations help users interpret prediction results easily.

## 🔧 Tech Stack
### Backend
- Python, Flask
- RandomForestRegressor (Scikit‑learn)
- MySQL (Connector/SQLAlchemy)

### Frontend
- HTML, CSS, Bootstrap
- Chart.js (for results visualization)

### Tools
- Pandas, NumPy
- Jupyter Notebook (model training)

## 🎯 Features
- Predict student exam scores based on:
  - Study hours
  - Attendance percentage
  - Internal assessment marks
- Random Forest ML model
- Real‑time score prediction using Flask API
- MySQL integration to store inputs & predictions
- Interactive charts using Chart.js
- Clean & responsive UI design

## 📊 ML Workflow
- Data preprocessing (cleaning, feature engineering)
- Model training using Random Forest
- Metrics: MAE, RMSE, R² Score
- Model saved as `.pkl` file
- Loaded dynamically in Flask during inference

## 🛠️ Installation & Setup

### 1. Clone the repository
```
git clone https://github.com/yourusername/exam-score-predictor.git
cd exam-score-predictor
```

### 2. Create a virtual environment
```
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Configure MySQL
Create database:
```
CREATE DATABASE exam_predictor;
```
Update DB credentials inside `config.py`.

### 5. Run the app
```
python app.py
```
Open browser: http://127.0.0.1:5000/

## 📁 Project Structure
```
Exam-Score-Predictor/
│── app.py
│── model.pkl
│── requirements.txt
│── templates/
│   └── index.html
│── static/
│   └── charts.js
│── config.py
│── database/
│   └── schema.sql
│── README.md
```

## ✍️ Author
**Fazin Firoz**  
Software Engineer | AI & Data Science  
Email: fazinzy@gmail.com  
GitHub: https://github.com/fazinfiroz
LinkedIn: https://linkedin.com/in/fazin-firoz-6aaa2825a
