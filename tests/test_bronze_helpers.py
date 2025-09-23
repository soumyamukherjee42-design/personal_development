import pandas as pd
import pytest
from tests.conftest import spark
from pyspark.sql import Row
from bronze.data_cleaning import clean_column_names, enforce_string_for_object_columns

def test_clean_column_names_pandas():
    # Given: a Pandas DataFrame with messy column names
    df = pd.DataFrame(columns=[" Col 1 ", "Col-2", "col 3__", "weird\tname", "eq=name"])
    
    # When: cleaning column names
    cleaned_df = clean_column_names(df)
    
    # Then: expected cleaned column names
    expected_columns = ["col_1", "col_2", "col_3", "weird_name", "eq_name"]
    assert cleaned_df.columns.tolist() == expected_columns


def test_enforce_string_for_object_columns():
    # Given: a DataFrame with object columns
    df = pd.DataFrame({
        "num": [1, 2],
        "text": ["abc", None],
        "mixed": [None, 3]
    })
    df["text"] = df["text"].astype("object")
    df["mixed"] = df["mixed"].astype("object")

    # When: converting object columns to strings
    result_df = enforce_string_for_object_columns(df)

    # Then: all object columns should now be strings
    assert result_df["text"].dtype == object
    assert result_df["mixed"].dtype == object
    assert all(isinstance(x, str) for x in result_df["text"])
    assert all(isinstance(x, str) for x in result_df["mixed"])


def test_clean_column_names_spark(spark):
    # Given: a Spark DataFrame with messy column names
    data = [(1, 2, 3, 4, 5)]
    columns = [" Col 1 ", "Col-2", "col 3__", "eq=name", " weird(name)"]
    df = spark.createDataFrame(data, columns)

    # When: cleaning column names
    cleaned_df = clean_column_names(df)

    # Then: expected column names after cleaning
    expected_columns = {"col_1", "col_2", "col_3", "eq_name", "weird_name"}
    assert set(cleaned_df.columns) == expected_columns
