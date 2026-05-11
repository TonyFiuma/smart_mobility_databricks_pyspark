from pyspark.sql.functions import col


# =========================
# READ BRONZE
# =========================
def read_bronze(spark, path):
    return spark.read.format("delta").load(path)


def transform_to_silver(df, column_mapping=None, cast_columns=None):

    # =========================
    # RENAME COLUMNS (OPTIONAL)
    # =========================
    if column_mapping:
        for old_col, new_col in column_mapping.items():
            if old_col in df.columns:
                df = df.withColumnRenamed(old_col, new_col)

    # =========================
    # REMOVE DUPLICATES
    # =========================
    df = df.dropDuplicates()

    # =========================
    # TYPE CASTING (OPTIONAL)
    # =========================
    if cast_columns:
        for col_name, col_type in cast_columns.items():
            if col_name in df.columns:
                df = df.withColumn(col_name, col(col_name).cast(col_type))

    return df


# =========================
# DATA QUALITY CHECKS
# =========================
def validate_silver(df, check_columns=None):
    """
    Generic validation layer.

    Parameters:
    - check_columns: list of columns to check for nulls
    """

    total = df.count()
    print(f"Total Silver rows: {total}")

    if check_columns:
        for c in check_columns:
            if c in df.columns:
                invalid = df.filter(col(c).isNull()).count()
                print(f"Invalid rows in '{c}': {invalid}")

    return df


# =========================
# WRITE SILVER
# =========================
def write_silver(df, path):
    df.write.format("delta") \
        .mode("overwrite") \
        .option("overwriteSchema", "true") \
        .save(path)