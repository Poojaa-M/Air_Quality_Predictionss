# air_quality_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import pickle

# Sample data (replace this with your real dataset)
data = {
    'Temperature': [15, 22, 27, 30, 25, 20, 18],
    'Humidity': [30, 40, 60, 70, 50, 55, 45],
    'Air_Quality_Index': [50, 55, 60, 65, 52, 54, 53]
}

# Load data into a DataFrame
df = pd.DataFrame(data)

# Split data into features and target variable
X = df[['Temperature', 'Humidity']]
y = df['Air_Quality_Index']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Decision Tree Regressor
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Save the model using pickle
with open('air_quality_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as air_quality_model.pkl")
