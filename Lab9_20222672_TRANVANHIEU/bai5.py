import pandas as pd
import numpy as np

# Đọc dữ liệu
df = pd.read_csv("suckhoe.csv")

# 1. Phát hiện Tuoi bất thường
invalid_age = df[(df["Tuoi"] <= 0) | (df["Tuoi"] > 100)]

print("Dòng có tuổi bất thường:")
print(invalid_age)

# 2. Phát hiện thiếu dữ liệu
print("\nKiểm tra dữ liệu thiếu:")
print(df.isna().sum())

# 3. Điền giá trị thiếu bằng trung vị
df["CanNang"] = df["CanNang"].fillna(df["CanNang"].median())
df["ChieuCao"] = df["ChieuCao"].fillna(df["ChieuCao"].median())

# 4. Chuẩn hóa NhomMau
df["NhomMau"] = (
    df["NhomMau"]
    .astype(str)
    .str.strip()
    .str.upper()
    .replace({
        "A": "A",
        "B": "B",
        "AB": "AB",
        "O": "O"
    })
)

# 5. Tính BMI
df["BMI"] = df["CanNang"] / ((df["ChieuCao"] / 100) ** 2)

# Làm tròn BMI
df["BMI"] = df["BMI"].round(2)

# Kết quả
print("\nDữ liệu sau xử lý:")
print(df)