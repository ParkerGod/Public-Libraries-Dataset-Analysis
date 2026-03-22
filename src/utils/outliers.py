"""Outlier detection and removal utilities."""
import pandas as pd


def remove_outliers_iqr(df, column, group_by):
    """Remove outliers using IQR method within each group.
    
    For each group defined by group_by column, calculate Q1, Q3 and IQR,
    then filter out values outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR].
    
    Args:
        df (pd.DataFrame): Input dataframe
        column (str): Column name to check for outliers
        group_by (str): Column name to group by before outlier removal
    
    Returns:
        pd.DataFrame: Dataframe with outliers removed
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
