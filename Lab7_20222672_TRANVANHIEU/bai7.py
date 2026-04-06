import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính cột DiemTB
df["DiemTB"] = (
    0.2 * df["DiemQT"]
    + 0.3 * df["DiemGK"]
    + 0.5 * df["DiemCK"]
)

# Tính điểm trung bình theo giới tính
tb_theo_gt = df.groupby("GioiTinh")["DiemTB"].mean()

# Làm tròn 2 chữ số thập phân
tb_theo_gt = tb_theo_gt.round(2)

print(tb_theo_gt)