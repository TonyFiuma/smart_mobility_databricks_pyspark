# 🏗️ Smart Mobility Data Architecture

## 📌 Overview

This document describes the architecture of the Smart Mobility data pipeline implemented on Databricks using the Medallion Architecture.

The pipeline processes raw urban mobility data and transforms it into analytics-ready datasets for business intelligence and dashboards.

---

## 🧱 Architecture Pattern

The project follows the **Medallion Architecture**:
Bronze → Silver → Gold → Serving Layer → Dashboard


---

## 🔄 Data Flow

### 1. Bronze Layer (Raw Data Ingestion)

- Source: CSV dataset (2011–2024 mobility data)
- Stored in Delta format
- No transformations applied
- Metadata added (ingestion timestamp)

**Purpose:** preserve raw data as-is

---

### 2. Silver Layer (Cleaned Data)

- Schema standardization
- Column renaming
- Type casting (numeric conversion)
- Duplicate removal

**Purpose:** create clean and reliable dataset for analytics

---

### 3. Gold Layer (Business Aggregation)

- Aggregation by:
  - year
  - vehicle_type
- KPI creation (total mobility usage)

**Purpose:** business-ready dataset for reporting and analytics

---

### 4. Serving Layer (SQL View)

- Creation of SQL view over Gold Delta table
- Enables easy querying for BI tools and dashboards

```sql
CREATE OR REPLACE VIEW smart_mobility_gold_vw AS
SELECT *
FROM delta.`/Volumes/dev/spark_db/datasets/smart_mobility/gold`;

5. Dashboard Layer
Built using Databricks SQL Dashboards
Visualizes:
Mobility trends over time
Vehicle type comparison
Evolution of urban mobility services

+-------------------+
|   CSV Dataset     |
+-------------------+
          ↓
+-------------------+
|   Bronze Layer    |
| Raw ingestion     |
+-------------------+
          ↓
+-------------------+
|   Silver Layer    |
| Cleaned data      |
+-------------------+
          ↓
+-------------------+
|    Gold Layer     |
| Aggregated KPIs   |
+-------------------+
          ↓
+-------------------+
|  SQL View Layer   |
| BI consumption    |
+-------------------+
          ↓
+-------------------+
|   Dashboard       |
| Insights & KPIs   |
+-------------------+

⚙️ Technologies Used
Databricks
Apache Spark (PySpark)
Delta Lake
SQL (Databricks Views)
Medallion Architecture

🚀 Design Principles
Scalability → Spark distributed processing
Separation of concerns → Bronze / Silver / Gold layers
Reusability → Gold dataset reused across analytics
Performance optimization → pre-aggregated KPIs
BI readiness → SQL view for dashboards

📊 Final Outcome

The architecture delivers a full end-to-end pipeline that transforms raw mobility data into:

Clean structured datasets
Aggregated business KPIs
Interactive dashboards for decision making