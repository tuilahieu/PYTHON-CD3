import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính cột DiemTB nếu chưa có
df["DiemTB"] = (
    0.2 * df["DiemQT"]
    + 0.3 * df["DiemGK"]
    + 0.5 * df["DiemCK"]
)

# Thống kê mô tả cột DiemTB
print("Trung bình:", round(df["DiemTB"].mean(), 2))
print("Lớn nhất:", round(df["DiemTB"].max(), 2))
print("Nhỏ nhất:", round(df["DiemTB"].min(), 2))
print("Độ lệch chuẩn:", round(df["DiemTB"].std(), 2))