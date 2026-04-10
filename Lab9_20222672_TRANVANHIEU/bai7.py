import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("khaosat.csv")

# 1. Chuẩn hóa CoLamThem về 1/0
df["CoLamThem"] = (
    df["CoLamThem"]
    .astype(str)
    .str.strip()
    .str.lower()
    .replace({
        "yes": 1, "y": 1, "có": 1, "co": 1,
        "no": 0, "n": 0, "không": 0, "khong": 0
    })
)

# 2. Chuẩn hóa MucDoHaiLong về thang 1–5
# (ép giá trị ngoài range về NaN rồi xử lý)
df["MucDoHaiLong"] = pd.to_numeric(df["MucDoHaiLong"], errors="coerce")
df.loc[(df["MucDoHaiLong"] < 1) | (df["MucDoHaiLong"] > 5), "MucDoHaiLong"] = None
df["MucDoHaiLong"] = df["MucDoHaiLong"].fillna(df["MucDoHaiLong"].median())

# 3. Đổi tên cột chuẩn
df = df.rename(columns={
    "MaSV": "ma_sv",
    "GioHocMoiNgay": "gio_hoc_moi_ngay",
    "MucDoHaiLong": "muc_do_hai_long",
    "CoLamThem": "co_lam_them"
})

# 4. Loại bản ghi có giờ học < 0
df = df[df["gio_hoc_moi_ngay"] >= 0]

# 5. Thống kê số sinh viên làm thêm và không làm thêm
counts = df["co_lam_them"].value_counts()

print("Số lượng sinh viên:")
print("Làm thêm:", counts.get(1, 0))
print("Không làm thêm:", counts.get(0, 0))

print("\nDữ liệu sau xử lý:")
print(df)