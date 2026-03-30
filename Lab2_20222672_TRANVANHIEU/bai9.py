n = int(input("Nhap so luong sinh vien: "))
ten = []
diem = []
for i in range(n):
    ho_ten = input("Nhap ho ten sinh vien thu " + str(i + 1) + ": ")
    x = float(input("Nhap diem: "))
    
    while x < 0 or x > 10:
        print("Diem khong hop le. Nhap lai!")
        x = float(input("Nhap diem: "))
    ten.append(ho_ten)
    diem.append(x)
tong = 0
dem_dat = 0
for i in range(n):
    print(ten[i], "-", diem[i])
    tong += diem[i]
    if diem[i] >= 5:
        dem_dat += 1

dtb = tong / n
max_diem = max(diem)
min_diem = min(diem)
vi_tri_max = diem.index(max_diem)
vi_tri_min = diem.index(min_diem)

print("Sinh vien cao nhat:", ten[vi_tri_max], "-", max_diem)
print("Sinh vien thap nhat:", ten[vi_tri_min], "-", min_diem)
print("So sinh vien dat:", dem_dat)
print("Diem trung binh:", round(dtb, 2))
if dtb >= 8:
    print("Nhan xet: Lop hoc tot")
elif dtb >= 6.5:
    print("Nhan xet: Lop hoc kha")
else:
    print("Nhan xet: Can cai thien")