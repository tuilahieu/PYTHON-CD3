import pandas as pd

# Tạo dữ liệu khảo sát
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05",
             "SV06", "SV07", "SV08", "SV09", "SV10"],
    "GioTuHoc": [3, 2, 1, 4, 2.5, 1.5, 3.5, 2, 1, 4],
    "SoBuoiNghi": [1, 2, 4, 0, 1, 3, 0, 2, 5, 1],
    "DiemCC": [9, 8, 6, 10, 8, 6, 9, 8, 5, 10],
    "DiemCuoiKy": [8, 7.5, 6, 9, 8, 6.5, 8.5, 7, 5.5, 9]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Tính điểm trung bình
df["DiemTB"] = 0.3 * df["DiemCC"] + 0.7 * df["DiemCuoiKy"]

# Hàm phân nhóm học tập
def nhom_hoc_tap(row):
    if row["GioTuHoc"] >= 3 and row["SoBuoiNghi"] <= 1:
        return "Tich cuc"
    elif row["GioTuHoc"] >= 2 and row["SoBuoiNghi"] <= 2:
        return "Binh thuong"
    else:
        return "Can ho tro"

# Tạo cột NhomHocTap
df["NhomHocTap"] = df.apply(nhom_hoc_tap, axis=1)

# Hiển thị toàn bộ dữ liệu
print("=== TOÀN BỘ DỮ LIỆU ===")
print(df)

# Lọc sinh viên tự học trên 2 giờ/ngày và nghỉ không quá 2 buổi
loc_sv = df[(df["GioTuHoc"] > 2) & (df["SoBuoiNghi"] <= 2)]

print("\n=== SINH VIÊN TỰ HỌC > 2 GIỜ VÀ NGHỈ <= 2 BUỔI ===")
print(loc_sv)

# Nhận xét xu hướng dữ liệu
print("\n=== NHẬN XÉT ===")
print("1. Sinh viên có số giờ tự học cao thường có điểm trung bình cao hơn.")
print("2. Những sinh viên nghỉ ít và tự học từ 3 giờ trở lên thường thuộc nhóm 'Tich cuc'.")
print("3. Sinh viên nghỉ nhiều hơn 2 buổi thường có xu hướng điểm thấp hơn.")
print("4. Nhóm 'Can ho tro' thường gồm các sinh viên tự học ít hoặc nghỉ nhiều.")
print("5. Điểm chuyên cần ảnh hưởng đến điểm trung bình nhưng điểm cuối kỳ có trọng số lớn hơn.")
print("6. Các sinh viên SV04, SV07 và SV10 có kết quả học tập nổi bật.")