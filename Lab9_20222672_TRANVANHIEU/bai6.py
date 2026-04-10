import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("sanpham.csv")

# 1. Loại bỏ ký tự tiền tệ và dấu phẩy trong Gia
df["Gia"] = (
    df["Gia"]
    .astype(str)
    .str.replace("đ", "", regex=False)
    .str.replace(",", "", regex=False)
)

# 2. Chuyển Gia sang số
df["Gia"] = df["Gia"].astype(int)

# 3. Chuẩn hóa DanhMuc về chữ thường
df["DanhMuc"] = df["DanhMuc"].astype(str).str.strip().str.lower()

# 4. Loại bỏ sản phẩm có SoLuongTon < 0
df = df[df["SoLuongTon"] >= 0]

# 5. Sắp xếp theo Gia giảm dần
df = df.sort_values(by="Gia", ascending=False)

# Kết quả
print("Dữ liệu sau xử lý:")
print(df)