import pandas as pd

df = pd.read_csv("lienhe.csv")

# 1. Chuẩn hóa email về chữ thường
df["Email"] = df["Email"].astype(str).str.strip().str.lower()

# 2. Kiểm tra email hợp lệ (regex đơn giản)
df["EmailHopLe"] = df["Email"].str.contains(r"^[\w\.-]+@[\w\.-]+\.\w+$")

# 3. Tách đầu số / mã vùng điện thoại
df["DauSo"] = df["SoDienThoai"].astype(str).str.extract(r"^(\+?84|0)")

# 4. Loại bỏ khoảng trắng thừa trong địa chỉ
df["DiaChi"] = (
    df["DiaChi"]
    .astype(str)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

# 5. Trích xuất domain email
df["Domain"] = df["Email"].str.extract(r"@([\w\.-]+)")

# Kết quả
print("Dữ liệu sau xử lý:")
print(df)