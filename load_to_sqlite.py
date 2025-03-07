import sqlite3
import pandas as pd

# Load CSV data into a Pandas DataFrame
csv_filename = "splunk_data.csv"
df = pd.read_csv(csv_filename)

# Connect to SQLite database (it will create a new DB file if not exists)
conn = sqlite3.connect("splunk_data.db")
cursor = conn.cursor()

# Create a dummy table (if not exists)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS splunk_data (
        timestamp TEXT,
        field1 TEXT,
        field2 TEXT
    )
""")
print("🛠️ Table created (if not exists).")

# Insert DataFrame rows into SQLite table
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO splunk_data (timestamp, field1, field2) VALUES (?, ?, ?)",
        (row["timestamp"], row["field1"], row["field2"])
    )

# Commit and close connection
conn.commit()
conn.close()
print("Data inserted successfully into SQLite DB!")
