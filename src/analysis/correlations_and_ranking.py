import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import matplotlib.pyplot as plt
import seaborn as sns
from src.data.loader import load_cleaned_data


def plot_correlations_and_ranking():
    df = load_cleaned_data()

    financial_service_cols = [
        "Operating Income Per Capita",
        "Operating Expenditures Per Capita",
        "Library Visits Per Capita Served",
        "Circulation Per Capita Served"
    ]
    correlation_matrix = df[financial_service_cols].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", fmt=".2f")
    plt.title("Correlation: Financial Health vs. Service Output")
    plt.tight_layout()
    plt.show()

    top_income = df.groupby("Library")["Operating Income Per Capita"].mean().nlargest(10).sort_values()
    top_visits = df.groupby("Library")["Library Visits Per Capita Served"].mean().nlargest(10).sort_values()

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    axes[0].barh(top_income.index, top_income.values, color="teal")
    axes[0].set_title("Top 10 Libraries by Avg. Operating Income Per Capita")
    axes[0].set_xlabel("Operating Income Per Capita")

    axes[1].barh(top_visits.index, top_visits.values, color="coral")
    axes[1].set_title("Top 10 Libraries by Avg. Visits Per Capita")
    axes[1].set_xlabel("Library Visits Per Capita")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_correlations_and_ranking()
