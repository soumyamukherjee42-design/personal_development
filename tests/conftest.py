# tests/conftest.py

import sys
import os
import pytest
from pyspark.sql import SparkSession

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

@pytest.fixture(scope="session")
def spark():
    # ✅ Use the active Spark session from Databricks, or create one if not present
    spark = SparkSession.getActiveSession()
    if spark is None:
        spark = SparkSession.builder.getOrCreate()
    return spark