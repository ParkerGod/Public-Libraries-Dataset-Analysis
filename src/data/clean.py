import pandas as pd
from config import RAW_DATA_PATH, CLEANED_DATA_PATH, ESSENTIAL_COLUMNS


def clean_data() -> pd.DataFrame:
    df = pd.read_csv(RAW_DATA_PATH)

    threshold = len(df) * 0.75
    df_cleaned = df.dropna(thresh=threshold, axis=1)

    df_cleaned = df_cleaned.dropna(subset=ESSENTIAL_COLUMNS)

    numeric_cols = df_cleaned.select_dtypes(include=["float64", "int64"]).columns
    df_cleaned[numeric_cols] = df_cleaned[numeric_cols].fillna(df_cleaned[numeric_cols].median())

    df_cleaned.columns = df_cleaned.columns.str.strip()

    df_cleaned.to_csv(CLEANED_DATA_PATH, index=False)
    print(f"Cleaned data saved to {CLEANED_DATA_PATH}")
    print(df_cleaned.head())

    return df_cleaned


if __name__ == "__main__":
    clean_data()
