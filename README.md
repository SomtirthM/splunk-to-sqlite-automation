# Splunk to Database Automation

## Overview
This project automates data extraction from **Splunk** and loads it into an **Oracle database** using Python.  
Currently, analysts manually download CSV files from Splunk multiple times a day.  
This solution removes manual intervention by automating the process end-to-end.

---

## Steps Covered in This Project:
Step 1: Setup Python Environment
Step 2: Fetch Data from Splunk API
 Step 3: Process Data using Pandas 
 Step 4: Load Data into Oracle DB 
 Step 5: Automate & Schedule Execution 
 Step 6: Implement Logging & Error Handling


## Installation & Setup

### **Set Up Python Environment**
Run the following commands in **Anaconda Prompt**:
```bash
conda create --name splunk_oracle_env python=3.9
conda activate splunk_oracle_env
conda install -c conda-forge requests pandas
pip install cx_Oracle
