ten = ["An", "Binh", "Chi", "Dung"]
diem = [7.5, 8.0, 6.5, 9.0]
tong = 0
dem_dat = 0
for i in range(len(ten)):
    print(ten[i], "-", diem[i])
    tong += diem[i]
    if diem[i] >= 5:
        dem_dat += 1

dtb = tong / len(diem)
max_diem = max(diem)
vi_tri = diem.index(max_diem)
print("Diem trung binh:", dtb)
print("Sinh vien cao nhat:", ten[vi_tri])
print("So sinh vien dat:", dem_dat)

if dtb >= 8:
    print("Ket luan: Lop hoc tot")
elif dtb >= 6.5:
    print("Ket luan: Lop hoc kha")
else:
    print("Ket luan: Can cai thien")