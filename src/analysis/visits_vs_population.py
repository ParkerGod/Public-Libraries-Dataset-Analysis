import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import matplotlib.pyplot as plt
from src.data.loader import load_cleaned_data


def plot_visits_vs_population():
    df = load_cleaned_data()
    print(df)

    df = df.rename(columns={
        "Population of Service Area": "Population",
        "Total Library Visits": "Visits",
        "Total Registered Borrowers": "Borrowers"
    })

    plt.figure(figsize=(8, 5))
    plt.scatter(df["Population"], df["Visits"], alpha=0.5, s=20, color="blue")
    plt.title("Library Visits vs Population Served")
    plt.xlabel("Population")
    plt.ylabel("Total Library Visits")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_visits_vs_population()
