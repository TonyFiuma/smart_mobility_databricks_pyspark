# Databricks notebook source
# MAGIC %md
# MAGIC # 📊 Dashboard Layer – SQL View Creation
# MAGIC
# MAGIC ## 📌 Objective
# MAGIC
# MAGIC This notebook defines the **serving layer** of the Smart Mobility pipeline.
# MAGIC
# MAGIC Its purpose is to expose the Gold dataset as a **SQL View**, enabling easy consumption by Databricks dashboards and BI tools.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🧠 Role in the Architecture
# MAGIC
# MAGIC The Medallion Architecture is composed of:
# MAGIC
# MAGIC | Layer  | Purpose |
# MAGIC |--------|--------|
# MAGIC | Bronze | Raw data ingestion |
# MAGIC | Silver | Cleaned and standardized data |
# MAGIC | Gold   | Aggregated business KPIs |
# MAGIC | View   | Data exposure for analytics and dashboards |
# MAGIC
# MAGIC The View layer acts as the **bridge between data engineering and business intelligence**.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ⚙️ Why a SQL View?
# MAGIC
# MAGIC Creating a view instead of directly querying the Gold table provides several advantages:
# MAGIC
# MAGIC - 📊 Simplified SQL queries for analysts
# MAGIC - 🔁 Reusable semantic layer for dashboards
# MAGIC - 🧩 Decoupling between storage and consumption
# MAGIC - 🚀 Faster and cleaner BI development
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 💾 Source Dataset
# MAGIC
# MAGIC The view is built on top of the **Gold Delta table**, which contains aggregated mobility KPIs:
# MAGIC
# MAGIC - `year`
# MAGIC - `vehicle_type`
# MAGIC - `total_value`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ⚙️ Implementation
# MAGIC
# MAGIC The view is created using a SQL statement in Databricks:
# MAGIC
# MAGIC ```sql
# MAGIC CREATE OR REPLACE VIEW smart_mobility_gold_vw AS
# MAGIC SELECT *
# MAGIC FROM delta.`/Volumes/dev/spark_db/datasets/smart_mobility/gold`;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE VIEW smart_mobility_gold_vw AS
# MAGIC SELECT *
# MAGIC FROM delta.`/Volumes/dev/spark_db/datasets/smart_mobility/gold`;