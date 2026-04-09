import sqlite3
import pandas as pd

# Kết nối tới file shop.db
conn = sqlite3.connect("shop.db")

# Đọc toàn bộ bảng orders vào DataFrame
df = pd.read_sql("SELECT * FROM orders", conn)

# Hiển thị 5 dòng đầu tiên
print("5 dòng đầu của bảng orders:")
print(df.head())

# In thông tin số dòng và số cột
print("\nKích thước dữ liệu:", df.shape)

# Tạo cột doanh thu
# DoanhThu = Quantity * Price
df["DoanhThu"] = df["Quantity"] * df["Price"]

# Tổng số đơn hàng
tong_don_hang = len(df)

# Tổng doanh thu
tong_doanh_thu = df["DoanhThu"].sum()

print("\nTổng số đơn hàng:", tong_don_hang)
print("Tổng doanh thu:", tong_doanh_thu)

# Đóng kết nối CSDL
conn.close()