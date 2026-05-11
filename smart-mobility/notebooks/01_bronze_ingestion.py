# Databricks notebook source
# MAGIC %md
# MAGIC # 🥉 Bronze Layer - Smart Mobility Dataset Ingestion
# MAGIC
# MAGIC ## 📌 Overview
# MAGIC
# MAGIC This notebook implements the **Bronze layer** of a Medallion Architecture pipeline using Databricks, Apache Spark, and Unity Catalog Volumes.
# MAGIC
# MAGIC The Bronze layer is responsible for ingesting raw data with minimal transformations while preserving the original dataset structure and adding basic ingestion metadata.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📊 Dataset Description
# MAGIC
# MAGIC The dataset contains information about **smart mobility services in Italy (2011–2024)**, including:
# MAGIC
# MAGIC - Bike sharing
# MAGIC - Car sharing
# MAGIC - Scooter sharing
# MAGIC - Electric scooters (monopattini)
# MAGIC
# MAGIC ### Key attributes:
# MAGIC - `anno` → year of observation
# MAGIC - `sharing_veicoli` → type of mobility service
# MAGIC - `sharing_veicoli_indicatori` → metric/indicator
# MAGIC - `sharing_veicoli_valore` → measured value
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📁 Data Sources & Storage
# MAGIC
# MAGIC ### Input (Raw Data - Unity Catalog Volume)
# MAGIC /Volumes/dev/spark_db/datasets/smart_mobility/ds574_dati_sharing_2011-2024.csv
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ⚙️ Processing Logic
# MAGIC
# MAGIC The notebook performs the following steps:
# MAGIC
# MAGIC 1. Reads raw CSV data using Spark
# MAGIC 2. Infers schema automatically
# MAGIC 3. Adds ingestion metadata (via reusable function in `src`)
# MAGIC 4. Writes data as Delta table in Bronze layer
# MAGIC 5. Displays final enriched dataset
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🧠 Code Architecture
# MAGIC
# MAGIC The notebook delegates core logic to the `src` layer:
# MAGIC
# MAGIC - `read_raw_csv(spark, input_path)`  
# MAGIC   → handles ingestion from Unity Catalog Volume
# MAGIC
# MAGIC - `add_ingestion_metadata(df)`  
# MAGIC   → adds audit column (`ingestion_timestamp`)
# MAGIC
# MAGIC - `write_bronze(df, path)`  
# MAGIC   → writes Delta Lake Bronze table
# MAGIC
# MAGIC This ensures separation between:
# MAGIC - 📓 Notebook (orchestration)
# MAGIC - 🧠 Business logic (`src` module)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🕒 Metadata
# MAGIC
# MAGIC Each record includes:
# MAGIC
# MAGIC - `ingestion_timestamp`: timestamp of ingestion into Databricks
# MAGIC
# MAGIC This enables:
# MAGIC - traceability
# MAGIC - auditing
# MAGIC - incremental pipeline evolution
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🥉 Bronze Layer Responsibilities
# MAGIC
# MAGIC The Bronze layer ensures:
# MAGIC
# MAGIC - Raw data preservation (no business transformations)
# MAGIC - Full reproducibility of ingestion
# MAGIC - Centralized ingestion logic
# MAGIC - Foundation for downstream Silver and Gold layers
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🏗 Medallion Architecture Position
# MAGIC Raw Data (CSV - Volumes)
# MAGIC ↓
# MAGIC 🥉 Bronze Layer (this notebook)
# MAGIC ↓
# MAGIC 🥈 Silver Layer (clean + transform)
# MAGIC ↓
# MAGIC 🥇 Gold Layer (aggregations / KPIs)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🚀 Execution Mode
# MAGIC
# MAGIC This notebook is currently designed for **manual execution** with hardcoded input/output paths. This choice is intentional for simplicity, clarity, and portfolio demonstration purposes, making the ingestion logic easier to read and test step-by-step.
# MAGIC
# MAGIC In a production scenario, the notebook is fully **parameterized using Databricks Widgets**, where `input_path` and `bronze_path` are dynamically passed from Databricks Workflows (Jobs). This allows the same codebase to be reused in automated pipelines without any code changes.
# MAGIC
# MAGIC Future production execution is therefore fully **workflow-driven**, with parameters managed externally by the orchestration layer.
# MAGIC
# MAGIC

# COMMAND ----------

import sys
import os

# =========================
# PATH SETUP
# =========================
repo_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.insert(0, repo_root + "/src")

from bronze_layer import (
    read_raw_csv,
    add_ingestion_metadata,
    write_bronze
)

# =========================
# INPUT / OUTPUT
# =========================
input_path = "/Volumes/dev/spark_db/datasets/smart_mobility/ds574_dati_sharing_2011-2024.csv"
bronze_path = "/Volumes/dev/spark_db/datasets/smart_mobility/bronze"

# =========================
# INGESTION PIPELINE
# =========================
df = read_raw_csv(spark, input_path)

bronze_df = add_ingestion_metadata(df)

print(f"Raw records ingested: {bronze_df.count()}")

write_bronze(bronze_df, bronze_path)

display(bronze_df)