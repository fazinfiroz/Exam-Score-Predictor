from flask import Flask, render_template, request
import dill
import numpy as np

app = Flask(__name__)

# Load trained model
with open('model.dill', 'rb') as f:
    model = dill.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    study_hours = float(request.form['study_hours'])
    attendance = float(request.form['attendance'])
    prediction = model.predict(np.array([[study_hours, attendance]]))[0]
    return render_template('index.html', 
                           prediction=round(prediction, 2),
                           study_hours=study_hours,
                           attendance=attendance)

if __name__ == '__main__':
    app.run(debug=True)
