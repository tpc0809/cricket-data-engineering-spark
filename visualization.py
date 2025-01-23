import os
import pandas as pd
import matplotlib.pyplot as plt

# Define directory and locate the correct CSV file
dir_path = "processed_cricket_data.csv"
if os.path.isdir(dir_path):
    csv_files = [f for f in os.listdir(dir_path) if f.startswith("part-") and f.endswith(".csv")]
    if not csv_files:
        raise FileNotFoundError("No valid CSV file found inside 'processed_cricket_data.csv' directory.")
    file_path = os.path.join(dir_path, csv_files[0])
else:
    raise FileNotFoundError(f"'{dir_path}' is not a directory or does not exist.")

# Load data
df = pd.read_csv(file_path)

# Convert relevant columns to numeric, dropping invalid values
df["batting_average"] = pd.to_numeric(df["batting_average"], errors="coerce")
df["runs"] = pd.to_numeric(df["runs"], errors="coerce")
df["matches"] = pd.to_numeric(df["matches"], errors="coerce")
df = df.dropna(subset=["batting_average", "runs", "matches"])

# Remove unrealistic outliers (e.g., batting averages above 100)
df = df[df["batting_average"] <= 100]

# Visualization: Runs vs. Batting Average
plt.figure(figsize=(10, 6))
plt.scatter(df["runs"], df["batting_average"], alpha=0.5, color="blue", edgecolors="black")
plt.xlabel("Total Runs", fontsize=12)
plt.ylabel("Batting Average", fontsize=12)
plt.title("Runs vs Batting Average", fontsize=14)
plt.grid(True)
plt.show()

# Visualization: Matches vs. Batting Average
plt.figure(figsize=(10, 6))
plt.scatter(df["matches"], df["batting_average"], alpha=0.5, color="green", edgecolors="black")
plt.xlabel("Total Matches", fontsize=12)
plt.ylabel("Batting Average", fontsize=12)
plt.title("Matches vs Batting Average", fontsize=14)
plt.grid(True)
plt.show()
