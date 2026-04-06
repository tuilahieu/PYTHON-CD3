import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Nếu chưa có cột DiemTB thì tính trước
df["DiemTB"] = (
    0.2 * df["DiemQT"]
    + 0.3 * df["DiemGK"]
    + 0.5 * df["DiemCK"]
)

# Hàm xếp loại
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

# Tạo cột XepLoai
df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# Hiển thị kết quả
print(df[["HoTen", "DiemTB", "XepLoai"]])