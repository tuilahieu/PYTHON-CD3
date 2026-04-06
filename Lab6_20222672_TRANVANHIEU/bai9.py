import pandas as pd

# Tạo DataFrame khách hàng
data = {
    "MaKH": ["KH01", "KH02", "KH03", "KH04", "KH05", "KH06", "KH07", "KH08"],
    "TenKH": ["Lan", "Minh", "Hung", "Ha", "Phuong", "Toan", "Ngoc", "Tuan"],
    "SoDonHang": [12, 5, 8, 15, 4, 10, 6, 3],
    "TongChiTieu": [25000000, 7200000, 12500000, 31000000,
                    4300000, 9800000, 15000000, 2800000]
}

df = pd.DataFrame(data)

# Hàm xếp loại khách hàng
def xep_loai(tien):
    if tien >= 20000000:
        return "VIP"
    elif tien >= 10000000:
        return "Than thiet"
    elif tien >= 5000000:
        return "Tiem nang"
    else:
        return "Thuong"

# Thêm cột xếp loại khách hàng
df["XepLoaiKH"] = df["TongChiTieu"].apply(xep_loai)

print("=== DANH SÁCH KHÁCH HÀNG ===")
print(df)

# Lọc khách hàng VIP và Thân thiết
print("\n=== KHÁCH HÀNG VIP VÀ THÂN THIẾT ===")
vip_thanthiet = df[df["XepLoaiKH"].isin(["VIP", "Than thiet"])]
print(vip_thanthiet)

# Sắp xếp theo tổng chi tiêu giảm dần
print("\n=== DANH SÁCH SẮP XẾP THEO TỔNG CHI TIÊU GIẢM DẦN ===")
sap_xep = df.sort_values(by="TongChiTieu", ascending=False)
print(sap_xep)

# Tính chi tiêu trung bình
chi_tieu_tb = df["TongChiTieu"].mean()

print("\n=== CHI TIÊU TRUNG BÌNH ===")
print(f"{chi_tieu_tb:,.0f} VND")