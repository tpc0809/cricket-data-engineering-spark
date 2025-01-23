import os
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Define the directory path
directory_path = "processed_cricket_data.csv"  # This is actually a folder, not a file

# Check if the path exists and is a directory
if not os.path.isdir(directory_path):
    print(f"Error: '{directory_path}' is not a directory or does not exist.")
    exit(1)

# Read all CSV files inside the directory and combine them
csv_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith(".csv")]

if not csv_files:
    print(f"Error: No CSV files found in '{directory_path}'.")
    exit(1)

# Load and concatenate all CSV parts
df = pd.concat([pd.read_csv(file, low_memory=False) for file in csv_files], ignore_index=True)

# Data Preprocessing - Handle missing values
df.replace("-", np.nan, inplace=True)  # Convert '-' to NaN
df.dropna(inplace=True)  # Remove rows with missing values

# Convert necessary columns to numerical format
df[['matches', 'runs', 'batting_average']] = df[['matches', 'runs', 'batting_average']].astype(float)

# Define features (X) and target variable (y)
X = df[['matches', 'runs']]
y = df['batting_average']

# Split the dataset into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Model evaluation
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Save the trained model
model_filename = "linear_regression_model.pkl"
with open(model_filename, "wb") as file:
    pickle.dump(model, file)

print(f"Model saved as '{model_filename}'")
