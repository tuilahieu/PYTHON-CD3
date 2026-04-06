import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính điểm trung bình học phần
df["DiemTB"] = (
    0.2 * df["DiemQT"]
    + 0.3 * df["DiemGK"]
    + 0.5 * df["DiemCK"]
)

# Phân nhóm điểm
bins = [0, 5, 7, 8.5, 10]
labels = ["<5", "5-6.9", "7-8.4", ">=8.5"]

df["NhomDiem"] = pd.cut(
    df["DiemTB"],
    bins=bins,
    labels=labels,
    right=False
)

# Thống kê số lượng sinh viên theo nhóm điểm của từng lớp
ket_qua = pd.crosstab(df["Lop"], df["NhomDiem"])

print(ket_qua)