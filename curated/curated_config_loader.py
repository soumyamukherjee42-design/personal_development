# curated_config_loader.py

import json

def load_curated_config(json_path: str) -> list:
    """
    Loads curated table definitions from a JSON config file.
    
    Args:
        json_path (str): Path to the JSON config file.
    
    Returns:
        List[dict]: List of curated table definitions.
    """
    with open(json_path, "r") as f:
        config = json.load(f)
    return config.get("curated_tables", [])
