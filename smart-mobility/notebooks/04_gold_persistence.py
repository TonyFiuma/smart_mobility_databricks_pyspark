# Databricks notebook source
# MAGIC %md
# MAGIC # 🥇 Gold Layer – Persistence Notebook
# MAGIC
# MAGIC ## 📌 Objective
# MAGIC
# MAGIC This notebook is responsible for persisting the **Gold layer** of the Smart Mobility pipeline into a Delta table.
# MAGIC
# MAGIC The Gold layer represents the **final business-ready dataset**, derived from the Silver layer through aggregations and KPI computations.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC
# MAGIC ## ⚙️ Gold Transformation Logic
# MAGIC
# MAGIC The Gold dataset is created by aggregating mobility data at a business level:
# MAGIC
# MAGIC - Grouping by `year`
# MAGIC - Grouping by `vehicle_type`
# MAGIC - Computing total usage value
# MAGIC
# MAGIC This provides a clear view of **mobility trends over time and across services**.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📊 Gold Dataset Schema
# MAGIC
# MAGIC The final Gold table contains:
# MAGIC
# MAGIC - `year` → reference year of observation  
# MAGIC - `vehicle_type` → type of mobility service (bike, car, scooter, etc.)  
# MAGIC - `total_value` → aggregated metric representing usage intensity  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 💾 Persistence Strategy
# MAGIC
# MAGIC Once the Gold dataset is generated, it is persisted as a **Delta table** in Databricks.
# MAGIC
# MAGIC This ensures:
# MAGIC - Reusability across multiple analytics notebooks
# MAGIC - Performance optimization for downstream queries
# MAGIC - Integration with BI tools (e.g., Databricks SQL, Power BI)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ⚙️ Implementation
# MAGIC
# MAGIC ```python
# MAGIC from pyspark.sql.functions import sum
# MAGIC
# MAGIC # Load Silver layer
# MAGIC silver_df = spark.read.format("delta") \
# MAGIC     .load("/Volumes/dev/spark_db/datasets/smart_mobility/silver")
# MAGIC
# MAGIC # Create Gold dataset (business aggregation)
# MAGIC gold_df = silver_df.groupBy("year", "vehicle_type").agg(
# MAGIC     sum("value").alias("total_value")
# MAGIC )
# MAGIC
# MAGIC display(gold_df)
# MAGIC
# MAGIC # Persist Gold layer
# MAGIC gold_df.write.format("delta") \
# MAGIC     .mode("overwrite") \
# MAGIC     .save("/Volumes/dev/spark_db/datasets/smart_mobility/gold")

# COMMAND ----------

from pyspark.sql.functions import sum

# -------------------------
# LOAD SILVER
# -------------------------
silver_df = spark.read.format("delta") \
    .load("/Volumes/dev/spark_db/datasets/smart_mobility/silver")

# -------------------------
# GOLD TRANSFORMATION
# -------------------------
gold_df = silver_df.groupBy("year", "vehicle_type").agg(
    sum("value").alias("total_value")
)

display(gold_df)

# -------------------------
# PERSIST GOLD LAYER
# -------------------------
gold_df.write.format("delta") \
    .mode("overwrite") \
    .save("/Volumes/dev/spark_db/datasets/smart_mobility/gold")