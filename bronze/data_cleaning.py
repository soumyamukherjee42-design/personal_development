# data_cleaning.py

import pandas as pd

def clean_column_names(df):
    if hasattr(df, "columns") and not hasattr(df, "withColumnRenamed"):  # Pandas
        new_cols = (
            pd.Series(df.columns)
            .str.strip()
            .str.replace(r"[ ,;{}()\n\t=-]", "_", regex=True)
            .str.replace(r"__+", "_", regex=True)
            .str.rstrip("_")
            .str.lower()
            .tolist()
        )
        df.columns = new_cols
        return df

    elif hasattr(df, "withColumnRenamed"):  # Spark
        new_cols = [
            col.strip()
            .replace("-", "_").replace(" ", "_").replace(",", "_").replace(";", "_")
            .replace("{", "_").replace("}", "_").replace("(", "_").replace(")", "_")
            .replace("\n", "_").replace("\t", "_").replace("=", "_")
            for col in df.columns
        ]
        new_cols = [c.lower() for c in new_cols]
        for old, new in zip(df.columns, new_cols):
            if old != new:
                df = df.withColumnRenamed(old, new)
        return df
    else:
        raise TypeError("Unsupported DataFrame type")

def enforce_string_for_object_columns(pdf: pd.DataFrame) -> pd.DataFrame:
    for col in pdf.select_dtypes(include=["object"]).columns:
        pdf[col] = pdf[col].astype(str)
    return pdf
