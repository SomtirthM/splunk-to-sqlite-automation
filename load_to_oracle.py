import cx_Oracle
import pandas as pd

# Database connection details (Update these with actual credentials)
DB_USERNAME = "your_username"
DB_PASSWORD = "your_password"
DB_DSN = "your_oracle_db_dsn"  # Example: "localhost/XEPDB1"

# Load CSV data into a Pandas DataFrame
csv_filename = "splunk_data.csv"
df = pd.read_csv(csv_filename)

# Establish Oracle connection
try:
    connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, DB_DSN)
    cursor = connection.cursor()
    print("Connected to Oracle Database!")

    # Create a dummy table (if not exists)
    cursor.execute("""
        CREATE TABLE splunk_data (
            timestamp VARCHAR2(50),
            field1 VARCHAR2(100),
            field2 VARCHAR2(100)
        )
    """)
    print("🛠️ Table created (if not exists).")

    # Insert DataFrame rows into Oracle table
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO splunk_data (timestamp, field1, field2) VALUES (:1, :2, :3)",
            (row["timestamp"], row["field1"], row["field2"])
        )

    # Commit and close connection
    connection.commit()
    print("Data inserted successfully into Oracle DB!")

except cx_Oracle.DatabaseError as e:
    print(f"Oracle DB Error: {e}")

finally:
    cursor.close()
    connection.close()
