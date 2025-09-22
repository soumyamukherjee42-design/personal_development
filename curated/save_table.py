# save_table.py

def save_as_curated_table(df, table_name: str):
    """
    Saves a Spark DataFrame as a Delta table with a 'curated_' prefix.
    
    Args:
        df (DataFrame): The Spark DataFrame to save.
        table_name (str): Base name of the table (without prefix).
    """
    full_table_name = f"curated_{table_name}"
    df.write.format("delta").mode("overwrite").saveAsTable(full_table_name)
    print(f"✅ Created table: {full_table_name}")
