import pandas as pd

# Đọc file JSON
df = pd.read_json("products.json")

# Chỉ lấy các cột cần thiết
ket_qua = df[["MaSP", "TenSP", "NhomHang", "Gia"]]

print(ket_qua)