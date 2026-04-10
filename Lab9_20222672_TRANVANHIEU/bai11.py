import pandas as pd
import numpy as np

df = pd.read_csv("tuyensinh.csv")

# =========================
# 1. CHUẨN HÓA DỮ LIỆU
# =========================

# Họ tên: viết thường + xóa khoảng trắng thừa + title case
df["HoTen"] = (
    df["HoTen"]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.title()
)

# Giới tính chuẩn hóa
df["GioiTinh"] = (
    df["GioiTinh"]
    .astype(str)
    .str.strip()
    .str.lower()
    .replace({
        "nam": "Nam",
        "nữ": "Nu",
        "nu": "Nu"
    })
)

# Ngày sinh chuẩn hóa
df["NgaySinh"] = pd.to_datetime(df["NgaySinh"], errors="coerce")

# =========================
# 2. XỬ LÝ THIẾU DỮ LIỆU
# =========================

# Điểm → ép số
for col in ["DiemToan", "DiemVan", "DiemAnh"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Fill NaN:
df["DiemToan"] = df["DiemToan"].fillna(df["DiemToan"].median())
df["DiemVan"] = df["DiemVan"].fillna(df["DiemVan"].median())
df["DiemAnh"] = df["DiemAnh"].fillna(df["DiemAnh"].median())

df["KhuVuc"] = df["KhuVuc"].fillna("Unknown")

# =========================
# 3. PHÁT HIỆN ĐIỂM LỖI
# =========================

df["DiemLoi"] = (
    (df["DiemToan"] < 0) | (df["DiemToan"] > 10) |
    (df["DiemVan"] < 0) | (df["DiemVan"] > 10) |
    (df["DiemAnh"] < 0) | (df["DiemAnh"] > 10)
)

print("Học sinh nhập điểm sai:")
print(df[df["DiemLoi"]])

# sửa điểm sai → đưa về median
for col in ["DiemToan", "DiemVan", "DiemAnh"]:
    median = df[col].median()
    df.loc[(df[col] < 0) | (df[col] > 10), col] = median

# =========================
# 4. TÍNH TỔNG ĐIỂM
# =========================

df["TongDiem"] = df["DiemToan"] + df["DiemVan"] + df["DiemAnh"]

# =========================
# 5. PHÂN NHÓM BẰNG QCUT
# =========================

df["XepLoai"] = pd.qcut(
    df["TongDiem"],
    q=4,
    labels=["Yeu", "TrungBinh", "Kha", "Gioi"]
)

# =========================
# 6. THỐNG KÊ THEO KHU VỰC
# =========================

thongke = df.groupby("KhuVuc").agg(
    SoLuong=("MaHS", "count"),
    DiemTB=("TongDiem", "mean"),
    MaxDiem=("TongDiem", "max"),
    MinDiem=("TongDiem", "min")
)

# =========================
# 7. XUẤT FILE
# =========================

df.to_csv("tuyensinh_clean.csv", index=False)
thongke.to_csv("thongke_khuvuc.csv")

print("\nDONE: Đã tạo file sạch + thống kê")