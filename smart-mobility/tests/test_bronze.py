import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, repo_root + "/src")

from pyspark.sql import SparkSession

from bronze_layer import add_ingestion_metadata

spark = SparkSession.builder.getOrCreate()


# =========================
# TEST METADATA COLUMN
# =========================
def test_add_ingestion_metadata():

    data = [
        (1, "bike"),
        (2, "car")
    ]

    columns = ["id", "vehicle"]

    df = spark.createDataFrame(data, columns)

    result = add_ingestion_metadata(df)

    assert "ingestion_timestamp" in result.columns

    assert result.count() == 2