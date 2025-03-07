import json
import time

# Simulating Splunk API JSON response
def fetch_splunk_data():
    print("📡 Simulating data fetch from Splunk API...")

    # Simulated JSON response (like what Splunk would return)
    sample_response = {
        "results": [
            {"timestamp": "2025-03-07 10:00:00", "field1": "value1", "field2": "value2"},
            {"timestamp": "2025-03-07 10:05:00", "field1": "value3", "field2": "value4"},
            {"timestamp": "2025-03-07 10:10:00", "field1": "value5", "field2": "value6"},
        ]
    }

    # Simulating API delay
    time.sleep(2)
    
    # Return data as a dictionary
    return sample_response

# Main execution
if __name__ == "__main__":
    data = fetch_splunk_data()
    print(json.dumps(data, indent=4))  # Pretty print JSON response
