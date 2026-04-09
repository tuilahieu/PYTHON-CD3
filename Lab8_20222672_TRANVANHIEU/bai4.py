import pandas as pd

# Ép cột MaKH thành kiểu chuỗi (string)
df = pd.read_csv(
    "customers.csv",
    dtype={"MaKH": str}
)

# Hiển thị dữ liệu
print(df)

# Kiểm tra kiểu dữ liệu của từng cột
print(df.dtypes)