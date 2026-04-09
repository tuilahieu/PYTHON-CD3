import pandas as pd

# Đọc từng sheet trong file Excel
hanghoa = pd.read_excel("inventory_3sheets.xlsx", sheet_name="HangHoa")
nhapkho = pd.read_excel("inventory_3sheets.xlsx", sheet_name="NhapKho")
xuatkho = pd.read_excel("inventory_3sheets.xlsx", sheet_name="XuatKho")

# Hiển thị 5 dòng đầu mỗi sheet
print("=== SHEET HANGHOA ===")
print(hanghoa.head())
print()

print("=== SHEET NHAPKHO ===")
print(nhapkho.head())
print()

print("=== SHEET XUATKHO ===")
print(xuatkho.head())