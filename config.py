import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 数据文件路径
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "Public_Libraries.csv")
CLEANED_DATA_PATH = os.path.join(BASE_DIR, "data", "Cleaned_Public_Libraries.csv")

# 数据清洗所需的关键字段
ESSENTIAL_COLUMNS = [
    "Population of Service Area",
    "Total Library Visits",
    "Fiscal Year"
]
