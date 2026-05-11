import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, repo_root + "/src")

from pyspark.sql import SparkSession

from gold_layer import (
    kpi_by_year,
    kpi_by_vehicle,
    kpi_by_vehicle_metric,
    rank_years,
    compare_vehicles,
    kpi_top_metrics
)

spark = SparkSession.builder.getOrCreate()


# =========================
# TEST KPI BY YEAR
# =========================
def test_kpi_by_year():

    data = [
        (2023, 100.0),
        (2023, 50.0),
        (2024, 200.0)
    ]

    columns = ["year", "value"]

    df = spark.createDataFrame(data, columns)

    result = kpi_by_year(df)

    rows = result.collect()

    result_dict = {row["year"]: row["total_value"] for row in rows}

    assert result_dict[2023] == 150.0
    assert result_dict[2024] == 200.0


# =========================
# TEST KPI BY VEHICLE
# =========================
def test_kpi_by_vehicle():

    data = [
        ("bike sharing", 100.0),
        ("bike sharing", 50.0),
        ("car sharing", 200.0)
    ]

    columns = ["vehicle_type", "value"]

    df = spark.createDataFrame(data, columns)

    result = kpi_by_vehicle(df)

    rows = result.collect()

    result_dict = {
        row["vehicle_type"]: row["total_value"]
        for row in rows
    }

    assert result_dict["bike sharing"] == 150.0
    assert result_dict["car sharing"] == 200.0


# =========================
# TEST KPI BY VEHICLE + METRIC
# =========================
def test_kpi_by_vehicle_metric():

    data = [
        ("bike sharing", "rides", 100.0),
        ("bike sharing", "rides", 50.0)
    ]

    columns = ["vehicle_type", "metric", "value"]

    df = spark.createDataFrame(data, columns)

    result = kpi_by_vehicle_metric(df)

    row = result.collect()[0]

    assert row["total_value"] == 150.0


# =========================
# TEST YEAR RANKING
# =========================
def test_rank_years():

    data = [
        (2023, 100.0),
        (2024, 300.0),
        (2025, 200.0)
    ]

    columns = ["year", "value"]

    df = spark.createDataFrame(data, columns)

    result = rank_years(df)

    rows = result.collect()

    rank_dict = {
        row["year"]: row["rank"]
        for row in rows
    }

    assert rank_dict[2024] == 1


# =========================
# TEST VEHICLE COMPARISON
# =========================
def test_compare_vehicles():

    data = [
        ("bike sharing", 100.0),
        ("car sharing", 200.0),
        ("scooter sharing", 300.0)
    ]

    columns = ["vehicle_type", "value"]

    df = spark.createDataFrame(data, columns)

    result = compare_vehicles(df)

    vehicles = [row["vehicle_type"] for row in result.collect()]

    assert "bike sharing" in vehicles
    assert "car sharing" in vehicles
    assert "scooter sharing" not in vehicles


# =========================
# TEST TOP METRICS
# =========================
def test_kpi_top_metrics():

    data = [
        ("rides", 100.0),
        ("rides", 50.0),
        ("users", 200.0)
    ]

    columns = ["metric", "value"]

    df = spark.createDataFrame(data, columns)

    result = kpi_top_metrics(df)

    rows = result.collect()

    result_dict = {
        row["metric"]: row["total_value"]
        for row in rows
    }

    assert result_dict["rides"] == 150.0
    assert result_dict["users"] == 200.0