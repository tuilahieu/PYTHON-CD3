import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính điểm trung bình học phần
df["DiemTB"] = (
    0.2 * df["DiemQT"]
    + 0.3 * df["DiemGK"]
    + 0.5 * df["DiemCK"]
)

# Tổng hợp theo lớp
tonghop = df.groupby("Lop")["DiemTB"].agg(
    SoLuong="count",
    TrungBinh="mean",
    CaoNhat="max",
    ThapNhat="min"
)

# Làm tròn cột điểm trung bình
tonghop["TrungBinh"] = tonghop["TrungBinh"].round(2)

print(tonghop)