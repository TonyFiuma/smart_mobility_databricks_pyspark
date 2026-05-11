import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, repo_root + "/src")

from pyspark.sql import SparkSession

from silver_layer import (
    transform_to_silver,
    validate_silver
)

spark = SparkSession.builder.getOrCreate()


# =========================
# TEST COLUMN RENAMING
# =========================
def test_transform_column_mapping():

    data = [
        (2024, "bike sharing", "rides", "100")
    ]

    columns = [
        "anno",
        "sharing_veicoli",
        "sharing_veicoli_indicatori",
        "sharing_veicoli_valore"
    ]

    df = spark.createDataFrame(data, columns)

    column_mapping = {
        "anno": "year",
        "sharing_veicoli": "vehicle_type",
        "sharing_veicoli_indicatori": "metric",
        "sharing_veicoli_valore": "value"
    }

    result = transform_to_silver(
        df,
        column_mapping=column_mapping
    )

    assert "year" in result.columns
    assert "vehicle_type" in result.columns
    assert "metric" in result.columns
    assert "value" in result.columns


# =========================
# TEST TYPE CASTING
# =========================
def test_transform_type_casting():

    data = [
        ("100",)
    ]

    columns = ["value"]

    df = spark.createDataFrame(data, columns)

    cast_columns = {
        "value": "double"
    }

    result = transform_to_silver(
        df,
        cast_columns=cast_columns
    )

    dtype = dict(result.dtypes)

    assert dtype["value"] == "double"


# =========================
# TEST REMOVE DUPLICATES
# =========================
def test_transform_drop_duplicates():

    data = [
        (1, "bike"),
        (1, "bike")
    ]

    columns = ["id", "vehicle"]

    df = spark.createDataFrame(data, columns)

    result = transform_to_silver(df)

    assert result.count() == 1


# =========================
# TEST VALIDATION
# =========================
def test_validate_silver():

    data = [
        (100.0,),
        (None,)
    ]

    columns = ["value"]

    df = spark.createDataFrame(data, columns)

    result = validate_silver(
        df,
        check_columns=["value"]
    )

    assert result.count() == 2