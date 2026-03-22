import pandas as pd

def remove_outliers_iqr(df, column, group_by):
    """
    使用IQR方法按分组移除异常值
    
    参数:
        df (pd.DataFrame): 输入数据框
        column (str): 需要处理异常值的列名
        group_by (str): 分组列名，按该列分组后分别计算IQR
    
    返回:
        pd.DataFrame: 移除异常值后的数据框
    """
    cleaned_df = pd.DataFrame()
    for group, subset in df.groupby(group_by):
        Q1 = subset[column].quantile(0.25)
        Q3 = subset[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        filtered = subset[(subset[column] >= lower_bound) & (subset[column] <= upper_bound)]
        cleaned_df = pd.concat([cleaned_df, filtered], axis=0)
    return cleaned_df

if __name__ == "__main__":
    # 测试函数
    from src.data.loader import load_cleaned_data
    
    df = load_cleaned_data()
    print("原始数据形状:", df.shape)
    
    df_no_outliers = remove_outliers_iqr(df, "Library Visits Per Capita Served", "County")
    print("移除异常值后数据形状:", df_no_outliers.shape)
