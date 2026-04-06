import pandas as pd

# Tạo DataFrame hóa đơn bán hàng
data = {
    "MaHD": ["HD01", "HD02", "HD03", "HD04", "HD05",
             "HD06", "HD07", "HD08", "HD09", "HD10"],

    "NgayBan": ["2026-04-01", "2026-04-01", "2026-04-02", "2026-04-02", "2026-04-03",
                "2026-04-03", "2026-04-04", "2026-04-04", "2026-04-05", "2026-04-05"],

    "TenSP": ["Laptop", "Chuot", "Man hinh", "USB", "Loa",
              "Tai nghe", "Laptop", "Webcam", "Ban phim", "Man hinh"],

    "SoLuong": [1, 5, 2, 10, 3, 4, 1, 2, 6, 1],

    "DonGia": [14500000, 150000, 2500000, 180000, 750000,
               450000, 14500000, 900000, 300000, 2500000],

    "NhanVien": ["An", "Binh", "An", "Chi", "Dung",
                 "Ha", "An", "Chi", "Binh", "Ha"]
}

df = pd.DataFrame(data)

# Tạo cột Thành Tiền
df["ThanhTien"] = df["SoLuong"] * df["DonGia"]

print("=== TOÀN BỘ HÓA ĐƠN ===")
print(df)

# Hiển thị 5 hóa đơn có giá trị cao nhất
print("\n=== 5 HÓA ĐƠN CÓ GIÁ TRỊ CAO NHẤT ===")
top5 = df.sort_values(by="ThanhTien", ascending=False).head(5)
print(top5)

# Lọc các hóa đơn có thành tiền >= 3.000.000
print("\n=== HÓA ĐƠN CÓ THÀNH TIỀN >= 3.000.000 ===")
print(df[df["ThanhTien"] >= 3000000])

# Tính tổng doanh thu
tong_doanh_thu = df["ThanhTien"].sum()

print("\n=== TỔNG DOANH THU ===")
print(f"{tong_doanh_thu:,} VND")