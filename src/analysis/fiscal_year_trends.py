"""Fiscal year trends analysis (circulation, program attendance, per capita metrics)."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.data.loader import load_cleaned_data


def plot_fiscal_year_trends():
    """Create line plots for fiscal year trends."""
    df = load_cleaned_data()
    
    # Set visual style
    sns.set(style="whitegrid")
    
    # --- EDA for Trends Over Time ---
    print("Unique Fiscal Years:", df["Fiscal Year"].nunique())
    print("Fiscal Year Range:", df["Fiscal Year"].min(), "to", df["Fiscal Year"].max())
    
    # Aggregate key metrics by Fiscal Year
    agg_df = df.groupby("Fiscal Year")[[
        "Total Circulation",
        "Total Program Attendance & Views"
    ]].sum().reset_index()
    
    # Summary Statistics
    print("\nSummary Statistics:")
    print(agg_df.describe())
    
    # Line Plots
    plt.figure(figsize=(14, 6))
    plt.plot(agg_df["Fiscal Year"], agg_df["Total Circulation"], marker='o', label="Total Circulation")
    plt.plot(agg_df["Fiscal Year"], agg_df["Total Program Attendance & Views"], marker='s', label="Program Attendance & Views")
    plt.title("Library Services Trends Over Time", fontsize=16)
    plt.xlabel("Fiscal Year")
    plt.ylabel("Total Metrics")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    # Percent Change Analysis
    pct_change = agg_df.set_index("Fiscal Year").pct_change() * 100
    print("\nYear-over-Year Percentage Change:")
    print(pct_change)
    
    df["Circulation Per Capita"] = df["Total Circulation"] / df["Population of Service Area"]
    df["Programs Per Capita"] = df["Total Program Attendance & Views"] / df["Population of Service Area"]
    per_capita_df = df.groupby("Fiscal Year")[["Circulation Per Capita", "Programs Per Capita"]].mean().reset_index()
    
    # Line plot for per capita trends
    plt.figure(figsize=(14, 6))
    plt.plot(per_capita_df["Fiscal Year"], per_capita_df["Circulation Per Capita"], marker='o', label="Circulation Per Capita")
    plt.plot(per_capita_df["Fiscal Year"], per_capita_df["Programs Per Capita"], marker='s', label="Programs Per Capita")
    plt.title("Per Capita Library Service Trends", fontsize=16)
    plt.xlabel("Fiscal Year")
    plt.ylabel("Average Per Capita Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_fiscal_year_trends()
