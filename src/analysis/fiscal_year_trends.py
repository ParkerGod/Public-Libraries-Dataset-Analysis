import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data.loader import load_cleaned_data

def plot_fiscal_year_trends():
    """绘制财年趋势图，包括流通量、活动参与度和人均指标的折线图"""
    df = load_cleaned_data()
    
    # 设置可视化风格
    sns.set(style="whitegrid")
    
    # --- EDA for Trends Over Time ---
    print("Unique Fiscal Years:", df["Fiscal Year"].nunique())
    print("Fiscal Year Range:", df["Fiscal Year"].min(), "to", df["Fiscal Year"].max())
    
    # 按财年聚合关键指标
    agg_df = df.groupby("Fiscal Year")[[
        "Total Circulation",
        "Total Program Attendance & Views"
    ]].sum().reset_index()
    
    # 摘要统计
    print("\nSummary Statistics:")
    print(agg_df.describe())
    
    # 折线图
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
    
    # 百分比变化分析
    pct_change = agg_df.set_index("Fiscal Year").pct_change() * 100
    print("\nYear-over-Year Percentage Change:")
    print(pct_change)
    
    # 计算人均指标
    df["Circulation Per Capita"] = df["Total Circulation"] / df["Population of Service Area"]
    df["Programs Per Capita"] = df["Total Program Attendance & Views"] / df["Population of Service Area"]
    per_capita_df = df.groupby("Fiscal Year")[["Circulation Per Capita", "Programs Per Capita"]].mean().reset_index()
    
    # 人均趋势折线图
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
