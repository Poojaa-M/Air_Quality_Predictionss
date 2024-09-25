# app.py
from flask import Flask, render_template, request
import pickle
import air_quality_model

app = Flask(__name__)

# Load the trained ML model
with open('air_quality_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])

    # Predict air quality index using the model
    prediction = model.predict([[temperature, humidity]])[0]

    # Render result on page
    return render_template('result.html', prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)
