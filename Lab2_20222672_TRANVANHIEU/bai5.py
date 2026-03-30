diem = float(input("Nhap diem tu 0 den 10: "))
while diem < 0 or diem > 10:
    print("Du lieu khong hop le, nhap lai.")
    diem = float(input("Nhap diem tu 0 den 10: "))
print("Diem hop le la:", diem)