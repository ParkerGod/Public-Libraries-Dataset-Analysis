import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA_PATH = DATA_DIR / "Public_Libraries.csv"
CLEANED_DATA_PATH = DATA_DIR / "Cleaned_Public_Libraries.csv"

ESSENTIAL_COLUMNS = ["Population of Service Area", "Total Library Visits", "Fiscal Year"]
