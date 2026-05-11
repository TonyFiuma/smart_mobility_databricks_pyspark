# Databricks notebook source
# MAGIC %md
# MAGIC # 🥇 Gold Layer - Business Analytics & KPI Generation
# MAGIC
# MAGIC ## 📌 Overview
# MAGIC
# MAGIC This notebook implements the **Gold layer** of a Medallion Architecture pipeline using Databricks and Apache Spark.
# MAGIC
# MAGIC The Gold layer transforms the cleaned Silver dataset into **business-ready insights and aggregated KPIs**, focusing on mobility trends and strategic analysis.
# MAGIC
# MAGIC The business logic is modularized in the `src` layer, while the notebook is responsible for orchestration and visualization of results.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎯 Objectives
# MAGIC
# MAGIC The Gold layer is designed to generate:
# MAGIC
# MAGIC - Mobility usage trends over time
# MAGIC - Service type comparisons (bike, car, scooter sharing)
# MAGIC - KPI aggregations by vehicle type and metric
# MAGIC - Ranking and prioritization of mobility indicators
# MAGIC - Business-ready datasets for dashboards and reporting
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📁 Data Source
# MAGIC
# MAGIC ### Input (Silver Layer - Delta Lake)
# MAGIC /Volumes/dev/spark_db/datasets/smart_mobility/silver
# MAGIC
# MAGIC
# MAGIC The Silver layer represents a **clean, validated, and standardized dataset**, ensuring reliable analytics.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ⚙️ Processing Logic
# MAGIC
# MAGIC All analytical transformations are implemented in:
# MAGIC
# MAGIC 📁 `src/gold_layer.py`
# MAGIC
# MAGIC ### Core functions:
# MAGIC
# MAGIC - `read_silver(spark, path)`
# MAGIC   → Loads Silver Delta dataset
# MAGIC
# MAGIC - `kpi_by_year(df)`
# MAGIC   → Total mobility usage per year
# MAGIC
# MAGIC - `kpi_by_vehicle(df)`
# MAGIC   → Aggregation by vehicle type
# MAGIC
# MAGIC - `kpi_by_vehicle_metric(df)`
# MAGIC   → Detailed breakdown by vehicle type and metric
# MAGIC
# MAGIC - `rank_years(df)`
# MAGIC   → Ranking of years based on total mobility usage
# MAGIC
# MAGIC - `compare_vehicles(df)`
# MAGIC   → Comparison between selected mobility services
# MAGIC
# MAGIC - `kpi_top_metrics(df)`
# MAGIC   → Most relevant mobility indicators
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📊 Key KPIs Generated
# MAGIC
# MAGIC ### 📈 1. Mobility trend over time
# MAGIC - Total usage aggregated by year
# MAGIC - Used to analyze growth of shared mobility services
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🚗 2. Vehicle type comparison
# MAGIC - Comparison between:
# MAGIC   - Bike sharing
# MAGIC   - Car sharing
# MAGIC   - Other mobility services
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📊 3. Metric-level analysis
# MAGIC - Breakdown by service type and metric
# MAGIC - Identifies dominant mobility indicators
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🏆 4. Year ranking
# MAGIC - Years ranked by total mobility usage
# MAGIC - Highlights peak adoption periods
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⚖️ 5. Service comparison
# MAGIC - Direct comparison of selected mobility services
# MAGIC - Useful for strategic urban planning insights
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔝 6. Top mobility metrics
# MAGIC - Identification of most impactful mobility indicators
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🧠 Why Gold Layer?
# MAGIC
# MAGIC The Gold layer represents the **business intelligence layer** of the pipeline:
# MAGIC
# MAGIC - Converts technical datasets into actionable insights
# MAGIC - Aggregates data for decision-making
# MAGIC - Supports dashboards and reporting tools
# MAGIC - Provides KPIs for stakeholders and urban planners
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🏗 Architecture Position
# MAGIC
# MAGIC RAW DATA (CSV - Volumes)
# MAGIC ↓
# MAGIC 🥉 Bronze Layer (raw ingestion)
# MAGIC ↓
# MAGIC 🥈 Silver Layer (clean + standardized data)
# MAGIC ↓
# MAGIC 🥇 Gold Layer (business KPIs & analytics)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🚀 Execution Mode
# MAGIC
# MAGIC This notebook is designed for **manual execution (portfolio mode)** with hardcoded input paths for clarity and simplicity.
# MAGIC
# MAGIC In production environments, the pipeline is fully **orchestrated via Databricks Workflows**, where the Silver path is dynamically passed as a parameter.
# MAGIC
# MAGIC The business logic remains fully reusable through the `src` module.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🔥 Key Design Principles
# MAGIC
# MAGIC - Separation of concerns (Notebook vs Business Logic)
# MAGIC - Reusable KPI functions in `src`
# MAGIC - Scalable medallion architecture
# MAGIC - Clean transformation from data engineering → analytics layer

# COMMAND ----------

import sys
import os

repo_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.insert(0, repo_root + "/src")

from gold_layer import (
    read_silver,
    kpi_by_year,
    kpi_by_vehicle,
    kpi_by_vehicle_metric,
    rank_years,
    compare_vehicles,
    kpi_top_metrics
)

silver_path = "/Volumes/dev/spark_db/datasets/smart_mobility/silver"

print("🥈 SILVER PATH:", silver_path)

silver_df = read_silver(spark, silver_path)

display(silver_df)

# =========================
# KPI 1 - YEAR TREND
# =========================
kpi_year = kpi_by_year(silver_df)
display(kpi_year.orderBy("year"))

# =========================
# KPI 2 - VEHICLE TYPE
# =========================
kpi_service = kpi_by_vehicle(silver_df)
display(kpi_service.orderBy("total_value", ascending=False))

# =========================
# KPI 3 - VEHICLE + METRIC
# =========================
kpi_metric = kpi_by_vehicle_metric(silver_df)
display(kpi_metric.orderBy("total_value", ascending=False))

# =========================
# KPI 4 - YEAR RANKING
# =========================
ranked_years = rank_years(silver_df)
display(ranked_years)

# =========================
# KPI 5 - COMPARISON BIKE vs CAR
# =========================
comparison = compare_vehicles(silver_df)
display(comparison.orderBy("total_value", ascending=False))

# =========================
# KPI 6 - TOP METRICS
# =========================
top_metrics = kpi_top_metrics(silver_df)
display(top_metrics.orderBy("total_value", ascending=False))