### Air Quality Prediction
## Project Overview
This project is a web-based application that predicts the Air Quality Index (AQI) based on environmental factors such as temperature and humidity. It combines a machine learning model with a user-friendly interface to provide real-time predictions based on user input.

## Key Features
# Machine Learning Model:

The model is built using a Decision Tree Regressor to predict the air quality index.
The model is trained on sample environmental data, or it can be trained with real AQI datasets.
The trained model is saved in a serialized form using Pickle for use within the web application.

# Web Application:

Built using the Flask framework to serve a simple and clean web interface.
Users can input temperature and humidity values to receive a predicted air quality index.
The app consists of:
Home page: Users input temperature and humidity.
Results page: Displays the predicted AQI based on the inputs.

# User Interface:

A purple background theme with a clean and minimalistic design.
Input forms are styled for ease of use and user-friendly experience.
