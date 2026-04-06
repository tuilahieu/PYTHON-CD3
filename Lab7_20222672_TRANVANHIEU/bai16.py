import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính điểm trung bình học phần
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

# Tổng hợp theo chuyên ngành
tong_hop_cn = df.groupby("ChuyenNganh").agg(
    SoSinhVien=("MaSV", "count"),
    DiemTrungBinh=("DiemTB", "mean")
)

# Đếm số sinh viên đạt A hoặc B
tyle_ab = (
    df[df["XepLoai"].isin(["A", "B"])]
    .groupby("ChuyenNganh")["MaSV"]
    .count()
)

# Ghép vào bảng tổng hợp
tong_hop_cn["SoDatAB"] = tyle_ab
tong_hop_cn["SoDatAB"] = tong_hop_cn["SoDatAB"].fillna(0)

# Tính tỷ lệ %
tong_hop_cn["TyLeDatAB"] = (
    tong_hop_cn["SoDatAB"] / tong_hop_cn["SoSinhVien"] * 100
)

# Làm tròn 2 chữ số
print(tong_hop_cn.round(2))