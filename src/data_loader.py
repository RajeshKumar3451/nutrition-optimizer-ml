import pandas as pd
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_csv_data(file_path: str) -> pd.DataFrame:
    """
    Loads a CSV file from a given path and returns a Pandas DataFrame.
    
    Args:
        file_path (str): The path to the CSV file.
        
    Returns:
        pd.DataFrame: The loaded data.
    """
    if not os.path.exists(file_path):
        logger.error(f"File not found at: {file_path}")
        raise FileNotFoundError(f"Check your 'data/raw/' folder for {file_path}")

    try:
        df = pd.read_csv(file_path)
        logger.info(f"Successfully loaded data with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        logger.error(f"An error occurred while loading the CSV: {e}")
        raise