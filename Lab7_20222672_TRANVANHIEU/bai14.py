import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính điểm trung bình học phần
df["DiemTB"] = (
    0.2 * df["DiemQT"]
    + 0.3 * df["DiemGK"]
    + 0.5 * df["DiemCK"]
)

# Tìm sinh viên có điểm trung bình cao nhất của từng lớp
idx = df.groupby("Lop")["DiemTB"].idxmax()

sv_max = df.loc[idx, ["HoTen", "Lop", "DiemTB"]]

print(sv_max)