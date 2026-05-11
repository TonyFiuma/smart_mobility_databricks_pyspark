from pyspark.sql.functions import current_timestamp


def read_raw_csv(spark, input_path):
    return spark.read.csv(
        input_path,
        header=True,
        inferSchema=True,
        sep=";"
    )


def add_ingestion_metadata(df):
    return df.withColumn(
        "ingestion_timestamp",
        current_timestamp()
    )


def write_bronze(df, bronze_path):
    df.write.format("delta") \
        .mode("overwrite") \
        .save(bronze_path)