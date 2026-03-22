import pandas as pd
from config import RAW_DATA_PATH, CLEANED_DATA_PATH

def load_raw_data():
    """
    加载原始未清洗的数据
    
    Returns:
        pd.DataFrame: 原始数据集
    """
    return pd.read_csv(RAW_DATA_PATH)

def load_cleaned_data():
    """
    加载已清洗的数据
    
    Returns:
        pd.DataFrame: 清洗后的数据集
    """
    return pd.read_csv(CLEANED_DATA_PATH)

if __name__ == "__main__":
    # 测试数据加载
    raw_df = load_raw_data()
    print("原始数据形状:", raw_df.shape)
    
    cleaned_df = load_cleaned_data()
    print("清洗后数据形状:", cleaned_df.shape)
    print("\n清洗后数据前5行:")
    print(cleaned_df.head())
