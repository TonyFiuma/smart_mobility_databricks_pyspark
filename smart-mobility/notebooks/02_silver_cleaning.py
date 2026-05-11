# Databricks notebook source
# MAGIC %md
# MAGIC # 🥈 Silver Layer - Data Cleaning, Standardization & Validation
# MAGIC
# MAGIC ## 📌 Overview
# MAGIC
# MAGIC This notebook implements the **Silver layer** of a Medallion Architecture pipeline using Databricks, Apache Spark, and Unity Catalog Volumes.
# MAGIC
# MAGIC The Silver layer transforms raw Bronze data into a **clean, standardized, and analytics-ready dataset**, using a modular transformation logic defined in the `src` layer.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎯 Objectives
# MAGIC
# MAGIC The main goals of the Silver layer are:
# MAGIC
# MAGIC - Standardize and optionally rename columns
# MAGIC - Apply safe type casting
# MAGIC - Remove duplicate records
# MAGIC - Perform basic data quality validation
# MAGIC - Prepare a clean dataset for downstream analytics (Gold layer)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ⚙️ Processing Logic (Modular Design)
# MAGIC
# MAGIC The Silver transformation is implemented in a reusable module:
# MAGIC
# MAGIC 📁 `src/silver_layer.py`
# MAGIC
# MAGIC ### Key functions:
# MAGIC
# MAGIC - `read_bronze(spark, path)`
# MAGIC   → Loads Bronze Delta table
# MAGIC
# MAGIC - `transform_to_silver(df, column_mapping, cast_columns)`
# MAGIC   → Applies:
# MAGIC   - column renaming (configurable)
# MAGIC   - duplicate removal
# MAGIC   - type casting
# MAGIC
# MAGIC - `validate_silver(df, check_columns)`
# MAGIC   → Performs data quality checks
# MAGIC
# MAGIC - `write_silver(df, path)`
# MAGIC   → Writes Delta Silver table
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🔄 Transformations Applied
# MAGIC
# MAGIC ### 1. Column Standardization (Config-driven)
# MAGIC
# MAGIC Column mapping is defined in the notebook:
# MAGIC
# MAGIC | Bronze Column | Silver Column |
# MAGIC |--------------|--------------|
# MAGIC | anno | year |
# MAGIC | sharing_veicoli | vehicle_type |
# MAGIC | sharing_veicoli_tipologia | service_type |
# MAGIC | sharing_veicoli_indicatori | metric |
# MAGIC | sharing_veicoli_valore | value |
# MAGIC
# MAGIC This mapping is passed dynamically to the transformation function.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 2. Data Cleaning
# MAGIC
# MAGIC - Removal of duplicate records
# MAGIC - Safe type casting of numeric fields (e.g., `value → double`)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 3. Data Quality Checks
# MAGIC
# MAGIC The pipeline performs basic validation:
# MAGIC
# MAGIC - Total number of records after transformation
# MAGIC - Count of invalid values (e.g., nulls in numeric columns like `value`)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📁 Data Sources
# MAGIC
# MAGIC ### Input (Bronze Layer - Delta Lake)
# MAGIC /Volumes/dev/spark_db/datasets/smart_mobility/bronze
# MAGIC
# MAGIC
# MAGIC ### Output (Silver Layer - Delta Lake)
# MAGIC /Volumes/dev/spark_db/datasets/smart_mobility/silver
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🧠 Why Silver Layer?
# MAGIC
# MAGIC The Silver layer represents the **trusted and cleaned dataset** in the Medallion Architecture:
# MAGIC
# MAGIC - Removes inconsistencies from raw data
# MAGIC - Standardizes schema across time and sources
# MAGIC - Enables reliable analytical queries
# MAGIC - Serves as the foundation for the Gold layer (business metrics)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🏗 Architecture Position
# MAGIC
# MAGIC RAW DATA (CSV in Volumes)
# MAGIC ↓
# MAGIC 🥉 Bronze Layer (raw ingestion + metadata)
# MAGIC ↓
# MAGIC 🥈 Silver Layer (clean + standardized + validated)
# MAGIC ↓
# MAGIC 🥇 Gold Layer (aggregated business KPIs)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🚀 Execution Mode
# MAGIC
# MAGIC This notebook is designed for **manual execution** with hardcoded input/output paths. This approach simplifies development, debugging, and portfolio presentation.
# MAGIC
# MAGIC In production environments, the pipeline is fully **parameterized via Databricks Workflows**, where `bronze_path` and `silver_path` are dynamically injected as job parameters.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🔥 Design Highlights
# MAGIC
# MAGIC - Modular transformation logic in `src/`
# MAGIC - Config-driven schema mapping
# MAGIC - Reusable across multiple datasets
# MAGIC - Clear separation between orchestration (notebook) and logic (code layer)

# COMMAND ----------

import sys
import os

repo_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.insert(0, repo_root + "/src")

from silver_layer import (
    read_bronze,
    transform_to_silver,
    validate_silver,
    write_silver
)

bronze_path = "/Volumes/dev/spark_db/datasets/smart_mobility/bronze"
silver_path = "/Volumes/dev/spark_db/datasets/smart_mobility/silver"

bronze_df = read_bronze(spark, bronze_path)

column_mapping = {
    "anno": "year",
    "sharing_veicoli": "vehicle_type",
    "sharing_veicoli_tipologia": "service_type",
    "sharing_veicoli_indicatori": "metric",
    "sharing_veicoli_valore": "value"
}

cast_columns = {
    "value": "double"
}

# =========================
# TRANSFORM TO SILVER
# =========================
silver_df = transform_to_silver(
    bronze_df,
    column_mapping=column_mapping,
    cast_columns=cast_columns
)

# =========================
# VALIDATION
# =========================
silver_df = validate_silver(
    silver_df,
    check_columns=["value"]
)

# =========================
# WRITE SILVER
# =========================
write_silver(silver_df, silver_path)

display(silver_df)