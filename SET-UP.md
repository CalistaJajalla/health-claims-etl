# 📁 Health Claims ETL Project Setup by Calista Jajalla ᓚᘏᗢ

## Table of Contents

1. [Project Folder Structure](#1-project-folder-structure)  
2. [About the Dataset](#2-about-the-dataset)  
3. [Setup Python Virtual Environment (venv)](#3-setup-python-virtual-environment-venv)  
4. [Docker Setup](#4-docker-setup)  
5. [Running the ETL Pipeline](#5-running-the-etl-pipeline)  
6. [Additional Project Files](#6-additional-project-files)  
   6.1 [create_tables.sql](#61-createtablessql)  
   6.2 [db.py](#62-dbpy)  
   6.3 [ml_model.py](#63-ml_modelpy)  
   6.4 [app.py (Streamlit Dashboard)](#64-apppy-streamlit-dashboard)  
       - 6.4.1 [Data Analytics Questions](#641-data-analytics-questions)  
       - 6.4.2 [Machine Learning Section](#642-machine-learning-section)  

---

## 1. Project Folder Structure

Make sure your project directory looks like this:

health-claims-etl/
├── README.md  
├── docker-compose.yml  
├── data/  
│   └── medical_insurance.csv  
├── etl/  
│   ├── etl.py                     # main ETL script  
│   ├── ml_model.py                # ML training script  
│   ├── db.py                      # Postgres connection  
│   ├── medical_cost_model.joblib  # saved model (after training). This file is about ~1 GB so its not in repo.
├── sql/  
│   └── create_tables.sql          # full warehouse schema  
├── streamlit_app/  
│   └── app.py                     # dashboard starter  
├── requirements.txt  
└── venv/                          # python virtualenv (gitignored)


## 2. About the Dataset

...

## 3. Setup Python Virtual Environment (venv)

...

## 4. Docker Setup

...

## 5. Running the ETL Pipeline

...

## 6. Additional Project Files

### 6.1 create_tables.sql

...

### 6.2 db.py

...

### 6.3 ml_model.py

...

### 6.4 app.py (Streamlit Dashboard)

...

#### 6.4.1 Data Analytics Questions

...

#### 6.4.2 Machine Learning Section

...
