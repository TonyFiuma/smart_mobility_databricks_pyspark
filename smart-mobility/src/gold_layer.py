from pyspark.sql.functions import col, sum, desc, dense_rank
from pyspark.sql.window import Window


# =========================
# READ SILVER
# =========================
def read_silver(spark, path):
    return spark.read.format("delta").load(path)


# =========================
# KPI 1 - YEAR
# =========================
def kpi_by_year(df):
    return df.groupBy("year").agg(
        sum("value").alias("total_value")
    )


# =========================
# KPI 2 - VEHICLE TYPE
# =========================
def kpi_by_vehicle(df):
    return df.groupBy("vehicle_type").agg(
        sum("value").alias("total_value")
    )


# =========================
# KPI 3 - VEHICLE + METRIC
# =========================
def kpi_by_vehicle_metric(df):
    return df.groupBy("vehicle_type", "metric").agg(
        sum("value").alias("total_value")
    )


# =========================
# KPI 4 - YEAR RANKING
# =========================
def rank_years(df):
    kpi = df.groupBy("year").agg(
        sum("value").alias("total_value")
    )

    window_spec = Window.orderBy(desc("total_value"))

    return kpi.withColumn(
        "rank",
        dense_rank().over(window_spec)
    )


# =========================
# KPI 5 - COMPARISON VEHICLES
# =========================
def compare_vehicles(df, vehicles=None):
    if vehicles is None:
        vehicles = ["bike sharing", "car sharing"]

    filtered = df.filter(col("vehicle_type").isin(vehicles))

    return filtered.groupBy("vehicle_type").agg(
        sum("value").alias("total_value")
    )


# =========================
# KPI 6 - TOP METRICS
# =========================
def kpi_top_metrics(df):
    return df.groupBy("metric").agg(
        sum("value").alias("total_value")
    )