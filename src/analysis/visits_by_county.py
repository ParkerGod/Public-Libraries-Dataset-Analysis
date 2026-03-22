import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.data.loader import load_cleaned_data
from src.utils.outliers import remove_outliers_iqr

def plot_visits_by_county():
    """绘制按县人均访问量箱线图"""
    df = load_cleaned_data()
    
    # 移除异常值
    df_no_outliers = remove_outliers_iqr(df, "Library Visits Per Capita Served", "County")
    
    # 设置seaborn风格
    sns.set(style="whitegrid")
    
    # 绘制移除异常值后的箱线图
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
