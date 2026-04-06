import pandas as pd

# Tạo Series lưu điểm của 5 sinh viên
diem_sv = pd.Series(
    [7.5, 8.0, 9.2, 6.8, 8.7],
    index=["SV001", "SV002", "SV003", "SV004", "SV005"]
)

# Hiển thị toàn bộ Series
print("Toàn bộ Series:")
print(diem_sv)

# Hiển thị hai phần tử đầu
print("\nHai phần tử đầu:")
print(diem_sv.head(2))

# Điểm lớn nhất
print("\nĐiểm lớn nhất:", diem_sv.max())

# Điểm trung bình
print("Điểm trung bình:", diem_sv.mean())

# Lọc sinh viên có điểm >= 8
print("\nSinh viên có điểm >= 8:")
print(diem_sv[diem_sv >= 8])