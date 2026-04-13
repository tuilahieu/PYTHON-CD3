import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# 2. Xem 5 dòng đầu
print("=== 5 dòng đầu ===")
print(df.head())

# 3. Thông tin tổng quan
print("\n=== Thông tin dữ liệu ===")
df.info()

# 4. Đếm giá trị thiếu
print("\n=== Giá trị thiếu từng cột ===")
print(df.isna().sum())