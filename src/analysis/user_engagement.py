import pandas as pd
import matplotlib.pyplot as plt
from src.data.loader import load_cleaned_data

def plot_user_engagement():
    """绘制用户参与度图表：持卡率、参考咨询、堆叠条形图、参与类型饼图"""
    df = load_cleaned_data()
    
    # ===== 条形图：持卡率 vs 参考咨询问题 =====
    plt.figure(figsize=(12, 6))
    plt.bar(df["Library"], df["Percent of Residents with Library Cards"], label="Library Card Holders (%)", color='skyblue')
    plt.plot(df["Library"], df["Reference Questions"], label="Reference Questions", color='coral', marker='o')
    plt.xticks(rotation=90)
    plt.title("Library Card Holders vs Reference Questions")
    plt.xlabel("Library")
    plt.ylabel("Engagement / Questions")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    # ===== 堆叠条形图：项目、参考问题、项目浏览量 =====
    stacked_df = df[["Library", "Total Programs (Synchronous + Prerecorded)", "Reference Questions", "Total Program Attendance & Views"]]
    stacked_df.set_index("Library", inplace=True)
    stacked_df = stacked_df.head(10)  # 限制显示数量以便于可视化
    stacked_df.plot(kind="bar", stacked=True, figsize=(14, 6), colormap="Paired")
    plt.title("Breakdown of User Engagement by Library (Top 10)")
    plt.xlabel("Library")
    plt.ylabel("Total Interactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # ===== 饼图：参与类型总体比例 =====
    total_programs = df["Total Programs (Synchronous + Prerecorded)"].sum()
    total_questions = df["Reference Questions"].sum()
    total_views = df["Total Program Attendance & Views"].sum()
    
    labels = ["Programs", "Reference Questions", "Program Attendance & Views"]
    sizes = [total_programs, total_questions, total_views]
    colors = ['lightgreen', 'gold', 'lightskyblue']
    
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title("Overall Breakdown of Engagement Types")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_user_engagement()
