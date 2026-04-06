import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv("diem_sinhvien.csv")

# Tạo cột điểm trung bình
df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

# Hàm xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.5:
        return "Trung bình"
    else:
        return "Yếu"

# Tạo cột XepLoai
df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# Lọc sinh viên có điểm trung bình >= 8
print("=== SINH VIÊN CÓ DIEMTB >= 8 ===")
print(df[df["DiemTB"] >= 8])

# Đổi tên cột HoTen thành TenSinhVien
df = df.rename(columns={"HoTen": "TenSinhVien"})

# Đặt MaSV làm chỉ mục
df = df.set_index("MaSV")

print("\n=== DATAFRAME SAU KHI XỬ LÝ ===")
print(df)