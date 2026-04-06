import pandas as pd

# -------------------------------
# Bài 1: Series điểm sinh viên
# -------------------------------
diem_sv = pd.Series(
    [7.5, 8.0, 9.2, 6.8, 8.7],
    index=["SV001", "SV002", "SV003", "SV004", "SV005"]
)

print("=== TOÀN BỘ SERIES ===")
print(diem_sv)

print("\n=== HAI PHẦN TỬ ĐẦU ===")
print(diem_sv.head(2))

print("\n=== ĐIỂM LỚN NHẤT ===")
print(diem_sv.max())

print("\n=== ĐIỂM TRUNG BÌNH ===")
print(diem_sv.mean())

print("\n=== SINH VIÊN CÓ ĐIỂM >= 8 ===")
print(diem_sv[diem_sv >= 8])

# -------------------------------
# Bài 2: DataFrame sinh viên
# -------------------------------
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05"],
    "HoTen": ["An", "Bình", "Chi", "Dũng", "Hà"],
    "Lop": ["CNTT1", "CNTT1", "CNTT2", "CNTT2", "CNTT1"],
    "DiemQT": [7.0, 8.5, 6.0, 9.0, 8.0],
    "DiemThi": [7.5, 8.0, 6.5, 9.5, 8.5]
}

# Tạo DataFrame
df = pd.DataFrame(data)

print("\n=== DATAFRAME BAN ĐẦU ===")
print(df)

# Chọn cột HoTen và DiemThi
print("\n=== CỘT HoTen VÀ DiemThi ===")
print(df[["HoTen", "DiemThi"]])

# Thêm cột điểm trung bình
df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

print("\n=== SAU KHI THÊM CỘT DiemTB ===")
print(df)

# Lọc sinh viên có điểm trung bình >= 8
print("\n=== SINH VIÊN CÓ DiemTB >= 8 ===")
print(df[df["DiemTB"] >= 8])

# Đổi tên cột HoTen thành TenSinhVien
df = df.rename(columns={"HoTen": "TenSinhVien"})

print("\n=== SAU KHI ĐỔI TÊN CỘT ===")
print(df)

# Đặt MaSV làm chỉ mục
df = df.set_index("MaSV")

print("\n=== SAU KHI ĐẶT MaSV LÀM INDEX ===")
print(df)