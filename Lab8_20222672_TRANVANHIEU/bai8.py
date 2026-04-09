import pandas as pd

# Đọc file sales.csv
df = pd.read_csv("sales.csv")

# Tạo cột doanh thu
# DoanhThu = SoLuong * DonGia
df["DoanhThu"] = df["SoLuong"] * df["DonGia"]

# Đặt ngưỡng doanh thu
nguong = 500000

# Lọc các đơn hàng có doanh thu lớn hơn ngưỡng
high_sales = df[df["DoanhThu"] > nguong]

# Hiển thị kết quả
print(high_sales)

# Ghi ra file CSV
high_sales.to_csv("high_sales.csv", index=False)

# Ghi ra file Excel
high_sales.to_excel("high_sales.xlsx", index=False)

print("Đã lưu file high_sales.csv và high_sales.xlsx")