import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv("diem_sinhvien.csv")

# Hiển thị thông tin tổng quan
print("=== 5 DÒNG ĐẦU ===")
print(df.head())

print("\n=== THÔNG TIN DỮ LIỆU ===")
df.info()

print("\n=== THỐNG KÊ MÔ TẢ ===")
print(df.describe())

# Tính cột DiemTB
df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

# Hàm xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7.0:
        return "Kha"
    elif diem >= 5.5:
        return "Trung binh"
    else:
        return "Yeu"

# Tạo cột XepLoai
df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# Lọc sinh viên đạt loại Khá trở lên
ket_qua = df[df["XepLoai"].isin(["Gioi", "Kha"])]

# Sắp xếp theo điểm trung bình giảm dần
ket_qua = ket_qua.sort_values(by="DiemTB", ascending=False)

# Hiển thị kết quả
print("\n=== DANH SÁCH SINH VIÊN ĐẠT LOẠI KHÁ TRỞ LÊN ===")
print(ket_qua)

# Lưu ra file CSV
ket_qua.to_csv("ketqua_xuly.csv", index=False, encoding="utf-8-sig")

print("\nĐã lưu file ketqua_xuly.csv")