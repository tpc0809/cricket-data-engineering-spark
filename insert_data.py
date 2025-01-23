import pandas as pd
import psycopg2
import numpy as np

# Load CSV file
df = pd.read_csv("Cricket_Dataset_Players.csv")

df = df.rename(columns={
    'Player Name': 'player_name',
    'Matches': 'matches',
    'Runs': 'runs',
    'Bowling Wickets': 'wickets',
    'Batting Average': 'batting_average',
    'Bowling Average': 'bowling_average'
})

# Select only necessary columns
expected_columns = ['player_name', 'matches', 'runs', 'wickets', 'batting_average', 'bowling_average']
df = df[expected_columns]

numeric_columns = ['matches', 'runs', 'wickets', 'batting_average', 'bowling_average']
df[numeric_columns] = df[numeric_columns].replace('-', np.nan).astype(float)

# Connect to PostgreSQL
conn = psycopg2.connect(database="cricket_db", user="tpc", password="Thot@1508", host="localhost", port="5432")
cursor = conn.cursor()

# Insert data
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO cricket_players (player_name, matches, runs, wickets, batting_average, bowling_average)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, [row['player_name']] + [None if pd.isna(value) else value for value in row[1:]])

conn.commit()
conn.close()

print("Data inserted successfully!")
