import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src.data.loader import load_cleaned_data

def plot_visits_vs_population():
    """绘制人口与访问量的散点图"""
    df = load_cleaned_data()
    
    df = df.rename(columns={
        'Population of Service Area': 'Population',
        'Total Library Visits': 'Visits',
        'Total Registered Borrowers': 'Borrowers'
    })

    # 散点图
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
