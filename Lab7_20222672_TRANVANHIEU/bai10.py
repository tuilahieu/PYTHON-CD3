import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính điểm trung bình
df["DiemTB"] = (
    0.2 * df["DiemQT"]
    + 0.3 * df["DiemGK"]
    + 0.5 * df["DiemCK"]
)

# Tạo cột xếp loại
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

# print(df[["MaSV", "Lop", "GioiTinh", "DiemTB", "XepLoai"]])

# Tạo pivot table theo lớp và xếp loại
pivot1 = pd.pivot_table(
    df,
    index="Lop",
    columns="XepLoai",
    values="MaSV",
    aggfunc="count",
    fill_value=0
)

print(pivot1)