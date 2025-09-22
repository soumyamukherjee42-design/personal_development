import pytest

@pytest.fixture(scope="session")
def spark():
    # Use the SparkSession provided by Databricks
    from pyspark.sql import SparkSession
    return SparkSession._instantiatedSession
