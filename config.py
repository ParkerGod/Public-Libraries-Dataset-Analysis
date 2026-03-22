"""Configuration file for Public Libraries Dataset Analysis."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

RAW_DATA_PATH = os.path.join(DATA_DIR, "Public_Libraries.csv")
CLEANED_DATA_PATH = os.path.join(DATA_DIR, "Cleaned_Public_Libraries.csv")

ESSENTIAL_COLUMNS = [
    "Population of Service Area",
    "Total Library Visits",
    "Fiscal Year"
]
