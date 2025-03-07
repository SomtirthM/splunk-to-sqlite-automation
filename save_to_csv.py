import json
import pandas as pd
from splunk_fetch import fetch_splunk_data  # Import function from previous script

# Fetch simulated data
data = fetch_splunk_data()

# Extract results from JSON
results = data.get("results", [])

# Convert to Pandas DataFrame
df = pd.DataFrame(results)

# Save to CSV
csv_filename = "splunk_data.csv"
df.to_csv(csv_filename, index=False)

print(f"Data saved to {csv_filename} successfully!")
print(df.head())  # Print first few rows
