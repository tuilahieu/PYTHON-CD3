import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính điểm trung bình học phần
df["DiemTB"] = (
    0.2 * df["DiemQT"]
    + 0.3 * df["DiemGK"]
    + 0.5 * df["DiemCK"]
)

# Tính điểm trung bình của từng lớp
tb_theo_lop = df.groupby("Lop")["DiemTB"].mean()

# Làm tròn 2 chữ số thập phân cho dễ nhìn
tb_theo_lop = tb_theo_lop.round(2)

print(tb_theo_lop)