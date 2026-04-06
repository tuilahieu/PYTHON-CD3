import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính DiemTB
df["DiemTB"] = (
    0.2 * df["DiemQT"]
    + 0.3 * df["DiemGK"]
    + 0.5 * df["DiemCK"]
)

# Tạo cột XepLoai
def xep_loai(diem):
    if diem >= 8.5:
        return "A"
    elif diem >= 7.0:
        return "B"
    elif diem >= 5.5:
        return "C"
    elif diem >= 4.0:
        return "D"
    else:
        return "F"

df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# Thống kê tần suất
print("Số lượng theo giới tính:")
print(df["GioiTinh"].value_counts())

print("\nSố lượng theo lớp:")
print(df["Lop"].value_counts())

print("\nSố lượng theo chuyên ngành:")
print(df["ChuyenNganh"].value_counts())

print("\nSố lượng theo xếp loại:")
print(df["XepLoai"].value_counts())