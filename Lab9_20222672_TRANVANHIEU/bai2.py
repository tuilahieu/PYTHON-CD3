import pandas as pd

# Đọc file CSV
df = pd.read_csv('donhang.csv')

# Hiển thị dữ liệu ban đầu
print('Dữ liệu ban đầu:')
print(df)

# Thông tin cơ bản
print('\nThông tin dữ liệu:')
print(df.info())

# 1. Kiểm tra các dòng bị trùng hoàn toàn
print('\nCác dòng bị trùng toàn bộ:')
print(df[df.duplicated()])

# 2. Kiểm tra trùng theo MaDon
print('\nCác dòng bị trùng theo MaDon:')
print(df[df.duplicated(subset='MaDon', keep=False)])

# 3. Giữ lại bản ghi đầu tiên, xóa các dòng trùng còn lại
# Xóa trùng toàn bộ trước

df = df.drop_duplicates()

# Sau đó xóa trùng theo MaDon, giữ lại dòng đầu tiên

df = df.drop_duplicates(subset='MaDon', keep='first')

# 4. Tạo cột ThanhTien = SoLuong * DonGia

df['ThanhTien'] = df['SoLuong'] * df['DonGia']

# 5. Chuyển cột NgayDat sang kiểu ngày tháng

df['NgayDat'] = pd.to_datetime(df['NgayDat'])

# Sắp xếp theo ngày đặt tăng dần

df = df.sort_values(by='NgayDat', ascending=True)

# Hiển thị dữ liệu sau khi xử lý
print('\nDữ liệu sau khi xử lý:')
print(df)

# Kiểm tra còn trùng theo MaDon không
print('\nSố lượng MaDon bị trùng còn lại:')
print(df['MaDon'].duplicated().sum())

# Lưu dữ liệu sau xử lý
output_file = 'donhang_sau_xu_ly.csv'
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f'\nĐã lưu file vào: {output_file}')