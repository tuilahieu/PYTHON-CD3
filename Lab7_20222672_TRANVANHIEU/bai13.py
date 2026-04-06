import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính điểm trung bình học phần
df["DiemTB"] = (
    0.2 * df["DiemQT"]
    + 0.3 * df["DiemGK"]
    + 0.5 * df["DiemCK"]
)

# Xếp hạng trong từng lớp
df["XepHangTrongLop"] = df.groupby("Lop")["DiemTB"].rank(
    ascending=False,
    method="dense"
)

# Hiển thị kết quả theo từng lớp
ket_qua = df[
    ["HoTen", "Lop", "DiemTB", "XepHangTrongLop"]
].sort_values(
    ["Lop", "XepHangTrongLop"]
)

print(ket_qua)