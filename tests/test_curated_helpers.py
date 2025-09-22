import os
import pytest
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from curated.save_table import save_as_curated_table

def test_save_as_curated_table_creates_table():
    # Define data and schema
    data = [(1, "A"), (2, "B")]
    schema = StructType([
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True)
    ])

    # Create DataFrame
    df = spark.createDataFrame(data=data, schema=schema)

    # Save the table
    table_name = "test_table"
    save_as_curated_table(df, table_name)

    # Verify
    result_df = spark.table(f"curated_{table_name}")
    assert result_df.count() == 2