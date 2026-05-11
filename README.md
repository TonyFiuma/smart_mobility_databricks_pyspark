# 🚀 Smart Mobility Data Pipeline (Databricks)



## 📌 Overview

This project implements an end-to-end **data engineering pipeline** on Databricks using the **Medallion Architecture (Bronze, Silver, Gold)** to analyze urban mobility services in Milan.

The goal is to transform raw mobility data into **business-ready KPIs and interactive dashboards**.

---
> ⚠️ **Important Note**  
> Some notebooks may appear to contain hardcoded file or table paths. This is intentional and done for **simplicity and portfolio demonstration purposes**.  
> 
> In a production environment, these values are fully **parameterized and dynamically passed via Databricks Jobs or Workflows**, ensuring flexibility, reusability, and environment independence.  
> 
> This approach allows the same codebase to be executed across different environments (dev, test, prod) without any code changes.
---

## 🏗️ Architecture

![Overview Image](images/Architecture.png)

The pipeline follows the Medallion architecture:

CSV Data
↓
Bronze (Raw ingestion)
↓
Silver (Cleaned & standardized data)
↓
Gold (Aggregated KPIs)
↓
SQL View (BI layer)
↓
Dashboard
---
All notebooks are orchestrating ETL logic implemented in the `src/` package for production-like modularity.

All notebooks orchestrate ETL logic implemented in the `src/` package for production-like modularity.

All notebooks are orchestrating ETL logic implemented in the `src/` package for production-like modularity.

                    ┌──────────────────────┐
                    │     CSV Dataset      │
                    └─────────┬────────────┘
                              ↓
                    ┌────────────────────────────────────────────┐
                    │   Bronze Layer                             │
                    │ Raw ingestion (Spark)                      │
                    │ 📓 01_bronze_ingestion.ipynb              │
                    │ 🧠 src/bronze_layer.py                     │
                    └─────────┬──────────────────────────────────┘
                              ↓
                    ┌────────────────────────────────────────────┐
                    │   Silver Layer                             │
                    │ Clean & standardize                        │
                    │ 📓 02_silver_cleaning.ipynb               │
                    │ 🧠 src/silver_layer.py                     │
                    └─────────┬──────────────────────────────────┘
                              ↓
                    ┌────────────────────────────────────────────┐
                    │    Gold Layer                              │
                    │ KPI Aggregations                           │
                    │ 📓 03_gold_analytics.ipynb                │
                    │ 🧠 src/gold_layer.py                      │
                    └─────────┬──────────────────────────────────┘
                              ↓
                    ┌──────────────────────────────────────┐
                    │   SQL / View Layer                   │
                    │ BI Consumption                       │
                    │ 📓 04_gold_persistence.ipynb         │
                    └─────────┬────────────────────────────┘
                              ↓
                    ┌──────────────────────────────────────┐
                    │    Dashboard                        │
                    │ Insights & KPIs                    │
                    │ 📓 05_dashboard_view.ipynb         │
                    └──────────────────────────────────────┘
                    └──────────────────────────────────────┘

---
## ⚙️ Tech Stack

- Databricks
- PySpark
- Delta Lake
- SQL (Databricks Views)
- Medallion Architecture

---

## 📊 Data Pipeline

### 1. Bronze Layer
- Raw CSV ingestion
- Metadata enrichment (ingestion timestamp)

### 2. Silver Layer
- Schema standardization
- Data cleaning & type casting
- Duplicate removal

### 3. Gold Layer
- KPI aggregation by year and vehicle type
- Business-level metrics preparation

### 4. Serving Layer
- SQL view creation for dashboard consumption

---

## 📈 Dashboard

The final dashboard includes:
- Mobility trends over time
- Comparison between vehicle types
- Evolution of urban mobility services

Built using Databricks SQL Dashboards.

---

## 📂 Repository Structure

notebooks/
01_bronze_ingestion.py
02_silver_cleaning.py
03_gold_analytics.py
04_gold_persistence.py
05_dashboard_view.sql

docs/
architecture.md


---

## 🚀 Key Insights

- Urban mobility increases steadily over time
- Bike sharing is the dominant service
- New mobility services (scooters, monopattini) emerge after 2019
- Strong diversification after 2020

---

## 🧠 Author Notes

This project demonstrates:
- End-to-end data engineering pipeline design
- Medallion architecture implementation
- ETL development with PySpark
- BI-ready dataset modeling

## 📬 Contact

For questions or collaboration:

📧 [axelfiumano@gmail.com](mailto:axelfiumano@gmail.com)
