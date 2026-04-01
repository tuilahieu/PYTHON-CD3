import pandas as pd
import numpy as np

# =========================
# 1. Tạo dữ liệu ban đầu
# =========================
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV03", "SV05", "SV06", "SV07", "SV08"],
    "Tuoi": [20, 21, 19, 19, None, 22, 35, 20],
    "GioiTinh": ["Nam", "Nữ", "nu", "nu", "Nam", "Nữ", "Nam", None],
    "GioTuHoc": [2.5, 3, None, 4, 2, 10, -1, 3.5],
    "GioMangXaHoi": [4, 5, 3.5, 3.5, 20, 2, 5, None],
    "DiemTB": [3.1, 2.8, 3.5, 3.5, 2.0, 3.8, 4.5, None]
}

df = pd.DataFrame(data)

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df)

# =========================
# 2. Kiểm tra kích thước dữ liệu
# =========================
print("\nKích thước dữ liệu:", df.shape)

# =========================
# 3. Kiểm tra dữ liệu thiếu
# =========================
print("\nSố lượng giá trị thiếu theo từng cột:")
print(df.isnull().sum())

# =========================
# 4. Xóa bản ghi trùng lặp theo MaSV
# =========================
df = df.drop_duplicates(subset="MaSV")

# =========================
# 5. Chuẩn hóa cột GioiTinh
# =========================
df["GioiTinh"] = df["GioiTinh"].replace({
    "nu": "Nữ",
    "Nữ": "Nữ",
    "Nam": "Nam"
})

df["GioiTinh"] = df["GioiTinh"].fillna("Không rõ")

# =========================
# 6. Điền dữ liệu thiếu bằng giá trị trung bình
# =========================
numeric_cols = ["Tuoi", "GioTuHoc", "GioMangXaHoi", "DiemTB"]

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# =========================
# 7. Phát hiện và xử lý dữ liệu bất thường
# =========================

# Tuổi > 30
df.loc[df["Tuoi"] > 30, "Tuoi"] = df["Tuoi"].mean()

# Giờ tự học < 0
df.loc[df["GioTuHoc"] < 0, "GioTuHoc"] = df["GioTuHoc"].mean()

# Giờ mạng xã hội > 12
df.loc[df["GioMangXaHoi"] > 12, "GioMangXaHoi"] = df["GioMangXaHoi"].mean()

# Điểm trung bình > 4.0
df.loc[df["DiemTB"] > 4.0, "DiemTB"] = df["DiemTB"].mean()

# =========================
# 8. In dữ liệu sau làm sạch
# =========================
print("\n=== DỮ LIỆU SAU LÀM SẠCH ===")
print(df)

# =========================
# 9. Chuẩn hóa Min-Max
# =========================
cols = ["Tuoi", "GioTuHoc", "GioMangXaHoi", "DiemTB"]

df_minmax = df.copy()

for col in cols:
    df_minmax[col] = (
        (df[col] - df[col].min()) /
        (df[col].max() - df[col].min())
    )

print("\n=== DỮ LIỆU SAU CHUẨN HÓA MIN-MAX ===")
print(df_minmax)

# =========================
# 10. Chuẩn hóa Z-score
# =========================
df_zscore = df.copy()

for col in cols:
    df_zscore[col] = (
        (df[col] - df[col].mean()) /
        df[col].std()
    )

print("\n=== DỮ LIỆU SAU CHUẨN HÓA Z-SCORE ===")
print(df_zscore)

# =========================
# 11. So sánh trước và sau chuẩn hóa
# =========================
print("\n=== NHẬN XÉT ===")
print("- Dữ liệu ban đầu có nhiều thang đo khác nhau.")
print("- Sau chuẩn hóa Min-Max, mọi giá trị nằm trong khoảng [0, 1].")
print("- Sau chuẩn hóa Z-score, dữ liệu có trung bình gần 0 và độ lệch chuẩn gần 1.")
print("- Chuẩn hóa giúp các biến được so sánh công bằng hơn khi phân tích hoặc xây dựng mô hình.")