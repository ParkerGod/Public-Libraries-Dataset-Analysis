"""Data cleaning utilities for Public Libraries Dataset Analysis."""
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import RAW_DATA_PATH, CLEANED_DATA_PATH, ESSENTIAL_COLUMNS


def clean_data():
    """Clean raw public libraries data and save to cleaned CSV.
    
    Cleaning steps:
    1. Drop columns with over 25% missing data
    2. Drop rows where essential fields are missing
    3. Fill remaining numeric NaN with median
    4. Standardize column names (remove trailing spaces)
    
    Returns:
        pd.DataFrame: Cleaned data
    """
    df = pd.read_csv(RAW_DATA_PATH)
    
    # Drop columns with over 25% missing data
    threshold = len(df) * 0.75
    df_cleaned = df.dropna(thresh=threshold, axis=1)
    
    # Drop rows where essential fields are missing
    df_cleaned = df_cleaned.dropna(subset=ESSENTIAL_COLUMNS)
    
    # Fill remaining numeric NaN with median
    numeric_cols = df_cleaned.select_dtypes(include=['float64', 'int64']).columns
    df_cleaned[numeric_cols] = df_cleaned[numeric_cols].fillna(df_cleaned[numeric_cols].median())
    
    # Standardize column names (remove trailing spaces)
    df_cleaned.columns = df_cleaned.columns.str.strip()
    
    # Save cleaned data
    df_cleaned.to_csv(CLEANED_DATA_PATH, index=False)
    
    return df_cleaned


if __name__ == "__main__":
    cleaned_df = clean_data()
    print(cleaned_df.head())
