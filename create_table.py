import psycopg2

conn = psycopg2.connect(
    database="cricket_db",
    user="tpc",  
    password="Thot@1508",  
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cricket_players (
        player_name TEXT,
        age INT,
        matches INT,
        runs INT,
        wickets INT,
        batting_average FLOAT,
        bowling_average FLOAT
    );
""")

conn.commit()
conn.close()

print("Table created successfully!")
