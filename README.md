# 🧱 Data Pipeline Project Structure

## 📁 Project Layers Overview

This project implements a modular data pipeline using **Apache Spark on Databricks**. It is divided into multiple layers:

---

### 1. 🟤 Raw Layer (Bronze)

**Purpose:**  
Initial ingestion and light transformation of raw data.

**Main Components:**
- `bronze/data_cleaning.py`
  - `clean_column_names(df)`: Standardizes column names.
  - `enforce_string_for_object_columns(df)`: Converts object-type columns to string.

**Tests:**
- `tests/test_bronze_helpers.py`: Unit tests for bronze layer helpers using PySpark.

---

### 2. 🟡 Curated Layer (Silver)

**Purpose:**  
Applies business rules and joins to transform raw data into structured curated tables.

**Main Components:**
- `curated/load_curated_tables.py`: Loads curated tables.
- `curated/save_table.py`: Saves DataFrames as Delta tables with a `curated_` prefix.
- `curated/__init__.py`: Initialization for curated package.

**Tests:**
- `tests/test_curated_helpers.py`: Validates save logic for curated tables.

---

### 3. 🟢 Business Layer (Gold)

**Purpose:**  
Performs aggregations and business-specific transformations.

**Main Components:**
- `business/aggregate_profit.py`: Aggregates profit by year, category, sub_category, and customer_name.
- `business/create_temp_views.py`: Executes SQL statements from a JSON config to create temporary views.

**Output Table:**
- `business_agg_profit`: Contains total profit by year and product category.

---

### 4. ✅ Testing

**Framework:** `pytest`

**Fixtures:**  
`tests/conftest.py` provides a shared SparkSession fixture:

python
@pytest.fixture(scope="session")
def spark():
    spark = SparkSession.getActiveSession()
    if spark is None:
        raise RuntimeError("Run tests inside a Databricks notebook with active SparkSession.")
    return spark


**🧪 How to Run Tests (from Notebook):**
bash
%sh
pytest ./tests/test_bronze_helpers.py
pytest ./tests/test_curated_helpers.py


---

## 🗂 Directory Structure


├── bronze/
│   └── data_cleaning.py
├── curated/
│   ├── load_curated_tables.py
│   ├── save_table.py
├── business/
│   ├── aggregate_profit.py
│   └── create_temp_views.py
├── tests/
│   ├── conftest.py
│   ├── test_bronze_helpers.py
│   └── test_curated_helpers.py
└── README.md