"""Data loading utilities for Public Libraries Dataset Analysis."""
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import RAW_DATA_PATH, CLEANED_DATA_PATH


def load_raw_data():
    """Load raw public libraries data from CSV.
    
    Returns:
        pd.DataFrame: Raw data from Public_Libraries.csv
    """
    return pd.read_csv(RAW_DATA_PATH)


def load_cleaned_data():
    """Load cleaned public libraries data from CSV.
    
    Returns:
        pd.DataFrame: Cleaned data from Cleaned_Public_Libraries.csv
    """
    return pd.read_csv(CLEANED_DATA_PATH)
