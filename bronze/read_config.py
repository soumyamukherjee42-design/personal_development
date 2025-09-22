import json

def read_from_config(relative_path: str):
    """
    Reads a JSON config file from the Git-based Databricks Repo.

    Parameters:
    - relative_path: str, path to config file relative to notebook

    Returns:
    - List of config entries
    """
    with open(relative_path, "r") as f:
        config_data = json.load(f)
    return config_data
