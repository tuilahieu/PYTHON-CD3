import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("muonsach.csv")

# 1. Chuyển ngày tháng
df["NgayMuon"] = pd.to_datetime(df["NgayMuon"])
df["NgayTra"] = pd.to_datetime(df["NgayTra"], errors="coerce")

# 2. Giữ nguyên bản ghi chưa trả sách (NgayTra NaT là hợp lệ)
# Không cần xóa gì ở bước này

# 3. Chuẩn hóa TrangThai
df["TrangThai"] = (
    df["TrangThai"]
    .astype(str)
    .str.strip()
    .str.lower()
    .replace({
        "da tra": "DaTra",
        "đã trả": "DaTra",
        "dã trả": "DaTra",
        "chua tra": "ChuaTra",
        "chưa trả": "ChuaTra",
        "chuatra": "ChuaTra"
    })
)

# 4. Thêm cột SoNgayMuon
# Nếu chưa trả sách thì lấy ngày hiện tại
today = pd.Timestamp("today").normalize()

df["SoNgayMuon"] = (df["NgayTra"].fillna(today) - df["NgayMuon"]).dt.days

# 5. Danh sách SV mượn quá 30 ngày
qua_30 = df[df["SoNgayMuon"] > 30]

print("Sinh viên mượn quá 30 ngày:")
print(qua_30)

# Kết quả
print("\nDữ liệu sau xử lý:")
print(df)