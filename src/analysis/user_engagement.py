import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import matplotlib.pyplot as plt
from src.data.loader import load_cleaned_data


def plot_user_engagement():
    df = load_cleaned_data()

    plt.figure(figsize=(12, 6))
    plt.bar(df["Library"], df["Percent of Residents with Library Cards"], label="Library Card Holders (%)", color="skyblue")
    plt.plot(df["Library"], df["Reference Questions"], label="Reference Questions", color="coral", marker="o")
    plt.xticks(rotation=90)
    plt.title("Library Card Holders vs Reference Questions")
    plt.xlabel("Library")
    plt.ylabel("Engagement / Questions")
    plt.legend()
    plt.tight_layout()
    plt.show()

    stacked_df = df[["Library", "Total Programs (Synchronous + Prerecorded)", "Reference Questions", "Total Program Attendance & Views"]]
    stacked_df = stacked_df.copy()
    stacked_df.set_index("Library", inplace=True)
    stacked_df = stacked_df.head(10)

    stacked_df.plot(kind="bar", stacked=True, figsize=(14, 6), colormap="Paired")
    plt.title("Breakdown of User Engagement by Library (Top 10)")
    plt.xlabel("Library")
    plt.ylabel("Total Interactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    total_programs = df["Total Programs (Synchronous + Prerecorded)"].sum()
    total_questions = df["Reference Questions"].sum()
    total_views = df["Total Program Attendance & Views"].sum()

    labels = ["Programs", "Reference Questions", "Program Attendance & Views"]
    sizes = [total_programs, total_questions, total_views]
    colors = ["lightgreen", "gold", "lightskyblue"]

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
    plt.title("Overall Breakdown of Engagement Types")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_user_engagement()
