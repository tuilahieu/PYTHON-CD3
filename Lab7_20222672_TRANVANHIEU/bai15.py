import pandas as pd
import numpy as np

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính điểm trung bình học phần
df["DiemTB"] = (
    0.2 * df["DiemQT"]
    + 0.3 * df["DiemGK"]
    + 0.5 * df["DiemCK"]
)

# Xác định kết quả đỗ / trượt
df["KetQua"] = np.where(df["DiemTB"] >= 4.0, "Do", "Truot")

# Thống kê số lượng
so_luong = pd.crosstab(df["Lop"], df["KetQua"])

print("Số lượng đỗ / trượt theo lớp:")
print(so_luong)

# Thống kê tỷ lệ %
ty_le = pd.crosstab(
    df["Lop"],
    df["KetQua"],
    normalize="index"
) * 100

print("\nTỷ lệ đỗ / trượt theo lớp (%):")
print(ty_le.round(2))