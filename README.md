###AIR QUALITY PREDICTION

##Project Overview:
This project aims to build a web-based application for predicting the Air Quality Index (AQI) based on environmental factors such as temperature and humidity. It combines machine learning (ML) for prediction and web development to create a user-friendly interface where users can input relevant data and receive a prediction for the air quality.

##Key Features:
#Machine Learning Model:

The core of the project is a Decision Tree Regressor machine learning model that predicts the air quality index based on temperature and humidity data.
The model is trained using sample data (or can be trained with real historical AQI datasets) and saved in a serialized form using Pickle for future use in the web application.

#Web Application:

A Flask-based web application serves as the user interface.
Users can enter temperature and humidity values into a form, and the app will predict the air quality index using the pre-trained model.
The app consists of two pages:
The Home page where users input the data.
The Results page where the predicted AQI is displayed.

#User Interface Design:

The UI features a purple background with a clean and minimalistic design.
Forms are styled for simplicity and user-friendliness, ensuring a smooth user experience.
