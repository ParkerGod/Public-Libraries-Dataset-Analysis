"""Population vs Library Visits scatter plot analysis."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.data.loader import load_cleaned_data


def plot_visits_vs_population():
    """Create scatter plot of library visits vs population served."""
    df = load_cleaned_data()
    print(df)

    df = df.rename(columns={
        'Population of Service Area': 'Population',
        'Total Library Visits': 'Visits',
        'Total Registered Borrowers': 'Borrowers'
    })

    # scatter plot
    plt.figure(figsize=(8, 5))
    plt.scatter(df['Population'], df['Visits'], alpha=0.5, s=20, color='blue')
    plt.title('Library Visits vs Population Served')
    plt.xlabel('Population')
    plt.ylabel('Total Library Visits')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_visits_vs_population()
