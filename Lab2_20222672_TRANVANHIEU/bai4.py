diem = [7.5, 8.0, 4.5, 6.0, 9.0, 5.5, 3.5]
tong = 0
dem_dat = 0
for x in diem:
    print(x)
    tong += x
    if x >= 5:
        dem_dat += 1
dtb = tong / len(diem)
print("Diem trung binh:", dtb)
print("Diem lon nhat:", max(diem))
print("So diem dat:", dem_dat)