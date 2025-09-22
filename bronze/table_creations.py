import json
from pyspark.sql import SparkSession
import pandas as pd
from data_cleaning import clean_column_names, enforce_string_for_object_columns

def create_managed_table_from_file(file_path: str, file_type: str, table_name: str, spark: SparkSession):
    """
    Reads a file of given type, cleans column names, enforces datatypes,
    and creates a managed Spark table.
    """
    file_type = file_type.lower()

    if file_type == "csv":
        df = spark.read.option("header", True).option("inferSchema", True).csv(file_path)
        df = clean_column_names(df)

    elif file_type == "json":
        with open(file_path, "r") as f:
            data = json.load(f)   # assumes full JSON array in file

        pdf = pd.DataFrame(data)
        pdf = clean_column_names(pdf)
        pdf = enforce_string_for_object_columns(pdf)  # ✅ fix for Arrow
        df = spark.createDataFrame(pdf)

    elif file_type == "excel":
        pdf = pd.read_excel(file_path)
        pdf = clean_column_names(pdf)
        pdf = enforce_string_for_object_columns(pdf)  # ✅ fix for Arrow
        df = spark.createDataFrame(pdf)

    else:
        raise ValueError(f"Unsupported file type: {file_type}")

    # ✅ Create managed Delta table
    df.write.format("delta").mode("overwrite").option("mergeSchema", "true").saveAsTable(table_name)

    print(f"✅ Managed table `{table_name}` created from `{file_path}`")
    return df
