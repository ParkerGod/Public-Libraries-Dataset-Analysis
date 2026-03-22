import pandas as pd
from config import RAW_DATA_PATH, CLEANED_DATA_PATH


def load_raw_data() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_PATH)


def load_cleaned_data() -> pd.DataFrame:
    return pd.read_csv(CLEANED_DATA_PATH)


if __name__ == "__main__":
    df = load_raw_data()
    print(df.head())
