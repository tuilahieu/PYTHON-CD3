import pandas as pd

# Đọc dữ liệu sinh viên từ CSV
students = pd.read_csv("students.csv")

# Đọc dữ liệu điểm từ Excel
scores = pd.read_excel("scores.xlsx")

# Ghép 2 bảng theo MaSV
merged = pd.merge(
    students,
    scores,
    on="MaSV",
    how="inner"
)

# Tính điểm tổng kết
# Ví dụ: 40% điểm quá trình + 60% điểm thi
merged["DiemTongKet"] = merged["DiemQT"] * 0.4 + merged["DiemThi"] * 0.6

# Chọn các cột cần hiển thị
bang_tong_hop = merged[[
    "MaSV",
    "HoTen",
    "Lop",
    "DiemQT",
    "DiemThi",
    "DiemTongKet"
]]

# Làm tròn điểm tổng kết đến 2 chữ số thập phân
bang_tong_hop["DiemTongKet"] = bang_tong_hop["DiemTongKet"].round(2)

# Hiển thị kết quả
print("Bảng tổng hợp điểm:")
print(bang_tong_hop)

# Lưu ra Excel
bang_tong_hop.to_excel("tonghop_diem.xlsx", index=False)

print("\nĐã lưu file tonghop_diem.xlsx")