import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("nhansu.csv")

# 1. Chuẩn hóa GioiTinh → Nam / Nữ
df["GioiTinh"] = (
    df["GioiTinh"]
    .astype(str)
    .str.strip()
    .str.lower()
    .replace({
        "nam": "Nam", "male": "Nam", "m": "Nam",
        "nu": "Nữ", "nữ": "Nữ", "female": "Nữ", "f": "Nữ"
    })
)

# 2. Chuẩn hóa PhongBan (viết hoa chữ cái đầu)
df["PhongBan"] = df["PhongBan"].astype(str).str.strip().str.title()

# 3. Xóa khoảng trắng thừa trong HoTen
df["HoTen"] = (
    df["HoTen"]
    .astype(str)
    .str.strip()
    .str.split()
    .str.join(" ")
)

# 4. Đổi tên cột sang chuẩn
df = df.rename(columns={
    "MaNV": "ma_nv",
    "HoTen": "ho_ten",
    "GioiTinh": "gioi_tinh",
    "PhongBan": "phong_ban",
    "Luong": "luong"
})

# Xem kết quả
print(df.head())

# Lưu file mới
df.to_csv("nhansu_sau_xu_ly.csv", index=False, encoding="utf-8-sig")