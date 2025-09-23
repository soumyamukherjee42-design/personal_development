import pytest
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from curated.save_table import save_as_curated_table
from pyspark.sql import SparkSession

spark = SparkSession.getActiveSession() or SparkSession.builder.getOrCreate()

def test_save_as_curated_table_creates_table():
    # Define test data and schema
    data = [(1, "A"), (2, "B")]
    schema = StructType([
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True)
    ])

    # Create DataFrame
    df = spark.createDataFrame(data=data, schema=schema)

    # Save table
    table_name = "test_table"
    save_as_curated_table(df, table_name)

    # Read table back and verify
    result_df = spark.table(f"curated_{table_name}")
    assert result_df.count() == 2
    assert set(result_df.columns) == {"id", "name"}
