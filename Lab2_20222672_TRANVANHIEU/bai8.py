ten = ["An", "Binh", "Chi", "Dung", "Ha"]
cc = [8.0, 7.5, 9.0, 6.5, 8.5]
gk = [7.0, 6.5, 8.5, 5.5, 7.5]
ck = [8.5, 6.0, 9.0, 5.0, 8.0]
dem_kha_gioi = 0
tong_lop = 0
for i in range(len(ten)):
    tong_ket = 0.1 * cc[i] + 0.3 * gk[i] + 0.6 * ck[i]
    tong_lop += tong_ket
    if tong_ket >= 8.5:
        xep_loai = "Gioi"
    elif tong_ket >= 7.0:
        xep_loai = "Kha"
    elif tong_ket >= 5.0:
        xep_loai = "Trung binh"
    else:
        xep_loai = "Chua dat"
    if xep_loai == "Gioi" or xep_loai == "Kha":
        dem_kha_gioi += 1
        print(ten[i], "-", round(tong_ket, 2), "-", xep_loai)
        
print("Diem trung binh lop:", round(tong_lop / len(ten), 2))
print("So sinh vien Kha/Gioi:", dem_kha_gioi)