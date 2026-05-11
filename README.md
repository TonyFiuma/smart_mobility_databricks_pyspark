# 🚀 Smart Mobility Data Pipeline (Databricks Medallion Architecture)
# TonyFiuma-smart-mobility-spark

---

## 📌 Overview

This project implements an end-to-end **data engineering pipeline** on Databricks using the **Medallion Architecture (Bronze, Silver, Gold)** to analyze urban mobility services in Italy.

The goal is to transform raw mobility data into **clean datasets, business KPIs, and dashboard-ready outputs**.

---

> ⚠️ **Important Note**  
Some notebooks may appear to contain hardcoded file or table paths. This is intentional and done for **simplicity and portfolio demonstration purposes**.  
In a production environment, all parameters are fully **dynamic and injected via Databricks Jobs or Workflows**, ensuring environment flexibility (dev/test/prod) without code changes.

---

## 🏗️ Architecture

![Overview Image](smart_mobility/images/ArchitectureDatabricks.png)

The pipeline follows the Medallion Architecture:
CSV Data
↓
Bronze Layer (Raw ingestion)
↓
Silver Layer (Clean & standardized data)
↓
Gold Layer (Aggregated KPIs)
↓
SQL View Layer (BI consumption)
↓
Dashboard (Insights & reporting)


---

## 🔧 Implementation Overview

All notebooks orchestrate ETL logic implemented in the `src/` package for production-like modularity.

┌────────────────────────────────────────────┐
│ Bronze Layer │
│ Raw ingestion (Spark) │
│ 📓 01_bronze_ingestion.ipynb

│ 🧠 bronze_layer.py

└────────────────────────────────────────────┘
↓
┌────────────────────────────────────────────┐
│ Silver Layer │
│ Clean & standardize │
│ 📓 02_silver_cleaning.ipynb

│ 🧠 silver_layer.py

└────────────────────────────────────────────┘
↓
┌────────────────────────────────────────────┐
│ Gold Layer │
│ KPI Aggregations │
│ 📓 03_gold_analytics.ipynb

│ 🧠 gold_layer.py

└────────────────────────────────────────────┘
↓
┌────────────────────────────────────────────┐
│ SQL / View Layer │
│ BI Consumption │
│ 📓 04_gold_persistence.ipynb

└────────────────────────────────────────────┘
↓
┌────────────────────────────────────────────┐
│ Dashboard │
│ Insights & KPIs │
│ 📓 05_dashboard_view.ipynb

└────────────────────────────────────────────┘

---

## ⚙️ Tech Stack

- Databricks
- PySpark
- Delta Lake
- SQL (Databricks Views)
- Medallion Architecture

---

## 📊 Pipeline Stages

### 🥉 Bronze Layer
- Raw CSV ingestion
- Metadata enrichment (ingestion timestamp)

### 🥈 Silver Layer
- Schema standardization
- Data cleaning & type casting
- Duplicate removal

### 🥇 Gold Layer
- KPI aggregation by year and vehicle type
- Business-ready metrics generation

### 📈 Serving Layer
- SQL views for BI tools and dashboards

---

## 📊 Dashboard

Final dashboards include:
- Urban mobility trends over time
- Comparison between vehicle types
- Evolution of shared mobility services

Built using **Databricks SQL Dashboards**.

---

## 📂 Repository Structure
notebooks/
├── 01_bronze_ingestion.ipynb
├── 02_silver_cleaning.ipynb
├── 03_gold_analytics.ipynb
├── 04_gold_persistence.ipynb
└── 05_dashboard_view.ipynb

src/
├── bronze_layer.py
├── silver_layer.py
└── gold_layer.py

docs/
└── architecture.md

---

## 🚀 Key Insights

- Urban mobility usage grows steadily over time
- Bike sharing is the dominant service
- New mobility services (scooters, monopattini) emerge after 2019
- Post-2020 diversification in mobility patterns

---

## 🧠 Project Highlights

This project demonstrates:
- End-to-end data engineering pipeline design
- Medallion architecture implementation
- Modular ETL development with PySpark
- Production-like code separation (`src/`)
- BI-ready dataset modeling

---

## 📬 Contact

For questions or collaboration:

📧 [axelfiumano@gmail.com](mailto:axelfiumano@gmail.com)

