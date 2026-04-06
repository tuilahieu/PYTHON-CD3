import pandas as pd

# Tạo DataFrame giao dịch
data = {
    "MaHD": ["HD01", "HD02", "HD03", "HD04", "HD05", "HD06",
             "HD07", "HD08", "HD09", "HD10", "HD11", "HD12"],

    "NhanVien": ["An", "Binh", "Chi", "An", "Dung", "Chi",
                 "An", "Binh", "Dung", "Chi", "An", "Binh"],

    "SoLuong": [1, 5, 2, 3, 1, 4, 2, 6, 1, 2, 1, 3],

    "DonGia": [14500000, 150000, 2500000, 750000, 900000, 450000,
               300000, 180000, 2500000, 900000, 14500000, 300000]
}

df = pd.DataFrame(data)

# Tạo cột doanh thu
df["DoanhThu"] = df["SoLuong"] * df["DonGia"]

print("=== DANH SÁCH GIAO DỊCH ===")
print(df)

# Tính tổng doanh thu của từng nhân viên
tong_nv = df.groupby("NhanVien")["DoanhThu"].sum().reset_index()

# Sắp xếp giảm dần theo doanh thu
tong_nv = tong_nv.sort_values(by="DoanhThu", ascending=False)

print("\n=== TỔNG DOANH THU THEO NHÂN VIÊN ===")
print(tong_nv)

# Xác định nhân viên có doanh thu cao nhất
nhan_vien_top = tong_nv.iloc[0]

print("\n=== NHÂN VIÊN CÓ DOANH THU CAO NHẤT ===")
print(nhan_vien_top)

# Nhận xét
print("\n=== NHẬN XÉT ===")
print("1. An là nhân viên có doanh thu cao nhất nhờ bán được nhiều sản phẩm giá trị lớn.")
print("2. Chi đứng thứ hai với doanh thu ổn định từ nhiều giao dịch khác nhau.")
print("3. Binh có số lượng giao dịch khá nhiều nhưng chủ yếu là sản phẩm giá thấp.")
print("4. Dung có ít giao dịch hơn nên doanh thu thấp hơn các nhân viên khác.")
print("5. Những giao dịch bán Laptop tạo ra phần lớn doanh thu của nhóm.")