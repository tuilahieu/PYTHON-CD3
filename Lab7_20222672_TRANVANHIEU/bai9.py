import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính điểm trung bình học phần
df["DiemTB"] = (
    0.2 * df["DiemQT"]
    + 0.3 * df["DiemGK"]
    + 0.5 * df["DiemCK"]
)

# Nhóm theo lớp và giới tính
baocao = df.groupby(["Lop", "GioiTinh"])["DiemTB"].agg(
    SoLuong="count",
    TrungBinh="mean",
    CaoNhat="max",
    ThapNhat="min"
)

# Làm tròn cột điểm trung bình
baocao["TrungBinh"] = baocao["TrungBinh"].round(2)

print(baocao)