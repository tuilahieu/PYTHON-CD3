import pandas as pd

# Đọc file CSV
df = pd.read_csv("students.csv")

# Hiển thị 5 dòng đầu
print(df.head())

# In số dòng và số cột
print("Số dòng, số cột:", df.shape)

# Hoặc tách riêng
print("Số dòng:", df.shape[0])
print("Số cột:", df.shape[1])

# Liệt kê tên các cột
print("Tên các cột:")
print(df.columns)