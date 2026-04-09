import requests
import pandas as pd

# Gọi API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# Chuyển dữ liệu JSON thành list Python
data = response.json()

# Đưa vào DataFrame
df = pd.DataFrame(data)

# Chọn các cột quan trọng
ket_qua = df[["id", "name", "email", "phone", "website"]]

# Đổi tên cột cho dễ hiểu
ket_qua.columns = [
    "MaNguoiDung",
    "HoTen",
    "Email",
    "SoDienThoai",
    "Website"
]

# Hiển thị dữ liệu
print("Dữ liệu lấy từ API:")
print(ket_qua.head())

# Lưu thành file CSV
ket_qua.to_csv("users_api.csv", index=False, encoding="utf-8-sig")

print("\nĐã lưu file users_api.csv")