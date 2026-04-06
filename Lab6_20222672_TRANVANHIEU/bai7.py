import pandas as pd

# Tạo DataFrame sản phẩm
data = {
    "MaSP": ["SP01", "SP02", "SP03", "SP04", "SP05", "SP06", "SP07", "SP08"],
    "TenSP": ["Chuot", "Ban phim", "Man hinh", "USB", "Laptop", "Loa", "Tai nghe", "Webcam"],
    "LoaiHang": [
        "Phu kien", "Phu kien", "Thiet bi", "Phu kien",
        "Thiet bi", "Thiet bi", "Phu kien", "Thiet bi"
    ],
    "DonGia": [150000, 300000, 2500000, 180000, 14500000, 750000, 450000, 900000],
    "SoLuongTon": [25, 18, 7, 40, 5, 12, 20, 8]
}

df = pd.DataFrame(data)

# Hiển thị toàn bộ dữ liệu
print("=== DANH SÁCH SẢN PHẨM ===")
print(df)

# Lọc sản phẩm có đơn giá > 500000
print("\n=== SẢN PHẨM CÓ ĐƠN GIÁ > 500000 ===")
print(df[df["DonGia"] > 500000])

# Tạo cột giá trị tồn kho
df["GiaTriTonKho"] = df["DonGia"] * df["SoLuongTon"]

print("\n=== SAU KHI THÊM CỘT GiaTriTonKho ===")
print(df)

# Sắp xếp theo giá trị tồn kho giảm dần
print("\n=== SẢN PHẨM SẮP XẾP THEO GIÁ TRỊ TỒN KHO GIẢM DẦN ===")
print(df.sort_values(by="GiaTriTonKho", ascending=False))

# Lọc sản phẩm có số lượng tồn < 10
print("\n=== SẢN PHẨM CÓ SỐ LƯỢNG TỒN < 10 ===")
print(df[df["SoLuongTon"] < 10])