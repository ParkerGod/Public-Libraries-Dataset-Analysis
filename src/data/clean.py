import pandas as pd
from config import RAW_DATA_PATH, CLEANED_DATA_PATH, ESSENTIAL_COLUMNS

def clean_data():
    """
    执行数据清洗流程:
    1. 删除缺失值超过25%的列
    2. 删除关键字段缺失的行
    3. 用中位数填充剩余数值型NaN值
    4. 标准化列名
    5. 保存清洗后的数据
    """
    # 加载原始数据
    df = pd.read_csv(RAW_DATA_PATH)
    
    # 删除缺失值超过25%的列
    threshold = len(df) * 0.75
    df_cleaned = df.dropna(thresh=threshold, axis=1)
    
    # 删除关键字段缺失的行
    df_cleaned = df_cleaned.dropna(subset=ESSENTIAL_COLUMNS)
    
    # 用中位数填充剩余数值型NaN值
    numeric_cols = df_cleaned.select_dtypes(include=['float64', 'int64']).columns
    df_cleaned[numeric_cols] = df_cleaned[numeric_cols].fillna(df_cleaned[numeric_cols].median())
    
    # 标准化列名（去除首尾空格）
    df_cleaned.columns = df_cleaned.columns.str.strip()
    
    # 保存清洗后的数据
    df_cleaned.to_csv(CLEANED_DATA_PATH, index=False)
    
    print("数据清洗完成！")
    print(f"清洗前数据形状: {df.shape}")
    print(f"清洗后数据形状: {df_cleaned.shape}")
    print("\n清洗后数据前5行:")
    print(df_cleaned.head())
    
    return df_cleaned

if __name__ == "__main__":
    clean_data()
