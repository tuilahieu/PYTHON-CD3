import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("data.csv")

# Xem 5 dòng đầu
print(df.head())

# Thông tin dữ liệu
print(df.info())

# Thống kê mô tả
print(df.describe())