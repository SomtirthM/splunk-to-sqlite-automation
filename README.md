## Splunk to Database Automation
## Overview

This project automates data extraction from **Splunk** and loads it into an **Oracle database** using Python.  
This solution removes manual effort and dependencies related to downloading CSV files from Splunk multiple times a day by automating the process end-to-end.


---

### Features
1. Automated Data Fetching – Uses the Splunk API to retrieve data.
2. Data Processing with Pandas – Converts JSON response into a structured DataFrame.
3. Database Integration – Stores fetched data into an SQLite database.
4. Scheduling & Automation – Runs at scheduled intervals using Task Scheduler.
5. Error Handling & Logging – Logs errors and successful executions.


This project automates data extraction from Splunk and loads it into an Oracle database using Python.
This solution removes manual effort and dependencies related to downloading CSV files from Splunk multiple times a day by automating the process end-to-end.

## Features
Automated Data Fetching – Uses the Splunk API to retrieve data.
Data Processing with Pandas – Converts JSON response into a structured DataFrame.
Database Integration – Stores fetched data into an SQLite database.
Scheduling & Automation – Runs at scheduled intervals using Task Scheduler.
Error Handling & Logging – Logs errors and successful executions.


## Installation & Setup


### **Set Up Python Environment**
Run the following commands in **Anaconda Prompt**:
```
conda create --name splunk_oracle_env python=3.9
conda activate splunk_oracle_env
pip install requests pandas sqlite3

```

## Clone This Repository
Run the following command to download the project:
```
git clone https://github.com/SomtirthM/splunk-to-sqlite-automation.git
cd splunk-to-sqlite-automation
```

## Run the Scripts
Fetch Data from Splunk & Save as CSV
```
python fetch_from_splunk.py
```

Load Data into SQLite
```
python load_to_sqlite.py
```


## 🗂️ Project Structure  

splunk-to-sqlite-automation/
│── fetch_from_splunk.py   # Simulates data fetching from Splunk
│── save_to_csv.py         # Saves fetched data as CSV
│── load_to_sqlite.py      # Loads CSV data into SQLite
│── config.py              # Configuration file
│── README.md              # Documentation
│── requirements.txt       # Dependencies

## Automating the Process
You can schedule this script using Windows Task Scheduler or Cron Job (Linux) to run at specific intervals.

## Contributions
Feel free to fork this repo, create a branch, make improvements, and submit a pull request! 

📜 License
This project is open-source and free to use.

