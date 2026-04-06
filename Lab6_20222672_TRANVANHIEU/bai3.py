import pandas as pd

# Đọc file CSV
df = pd.read_csv("diem_sinhvien.csv")

# Hiển thị 5 dòng đầu
print("=== 5 DÒNG ĐẦU ===")
print(df.head())

# Hiển thị 5 dòng cuối
print("\n=== 5 DÒNG CUỐI ===")
print(df.tail())

# Hiển thị thông tin dữ liệu
print("\n=== THÔNG TIN DỮ LIỆU ===")
df.info()

# Hiển thị thống kê mô tả
print("\n=== THỐNG KÊ MÔ TẢ ===")
print(df.describe())

# Số dòng và số cột
so_dong, so_cot = df.shape
print("\n=== KÍCH THƯỚC DỮ LIỆU ===")
print("Số dòng:", so_dong)
print("Số cột:", so_cot)

# Danh sách tên cột
print("\n=== TÊN CÁC CỘT ===")
print(df.columns.tolist())