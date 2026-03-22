"""Box plot of library visits per capita by county (with outlier removal)."""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.data.loader import load_cleaned_data
from src.utils.outliers import remove_outliers_iqr


def plot_visits_by_county():
    """Create box plot of library visits per capita by county."""
    df = load_cleaned_data()
    
    df_no_outliers = remove_outliers_iqr(df, "Library Visits Per Capita Served", "County")
    
    # Set seaborn style
    sns.set(style="whitegrid")
    
    # Plot box plot without outliers
    plt.figure(figsize=(12, 6))
    sns.boxplot(
        x="County",
        y="Library Visits Per Capita Served",
        data=df_no_outliers,
        palette="Set2"
    )
    plt.title("Library Visits Per Capita by County (Outliers Removed)")
    plt.xlabel("County")
    plt.ylabel("Library Visits Per Capita")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_visits_by_county()
