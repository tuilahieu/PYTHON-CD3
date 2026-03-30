
ho_ten = input("Nhập họ tên sinh viên: ")
diem_qua_trinh = float(input("Nhập điểm quá trình: "))
diem_thi = float(input("Nhập điểm thi: "))

diem_tb = 0.4 * diem_qua_trinh + 0.6 * diem_thi

if diem_tb >= 8.0:
    xep_loai = "Giỏi"
elif diem_tb >= 6.5:
    xep_loai = "Khá"
elif diem_tb >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Chưa đạt"

print("\nKẾT QUẢ:")
print("Họ tên:", ho_ten)
print("Điểm trung bình:", round(diem_tb, 2))
print("Xếp loại:", xep_loai)