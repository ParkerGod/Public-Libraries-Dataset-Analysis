import pandas as pd


def remove_outliers_iqr(df: pd.DataFrame, column: str, group_by: str) -> pd.DataFrame:
    """
    Remove outliers from a DataFrame using the IQR method, grouped by a specified column.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame containing the data.
    column : str
        The name of the column from which to remove outliers.
    group_by : str
        The name of the column to group by before calculating IQR bounds.

    Returns
    -------
    pd.DataFrame
        A DataFrame with outliers removed, preserving the original index structure.
    """
    cleaned_df = pd.DataFrame()
    for group, subset in df.groupby(group_by):
        Q1 = subset[column].quantile(0.25)
        Q3 = subset[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        filtered = subset[(subset[column] >= lower_bound) & (subset[column] <= upper_bound)]
        cleaned_df = pd.concat([cleaned_df, filtered], axis=0)
    return cleaned_df


if __name__ == "__main__":
    import sys
    sys.path.insert(0, ".")
    from src.data.loader import load_cleaned_data
    df = load_cleaned_data()
    df_no_outliers = remove_outliers_iqr(df, "Library Visits Per Capita Served", "County")
    print(f"Original rows: {len(df)}, After removing outliers: {len(df_no_outliers)}")
