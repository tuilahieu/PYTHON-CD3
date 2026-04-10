import pandas as pd

# Đọc file CSV
df = pd.read_csv('diem_sinhvien.csv')

# Hiển thị 5 dòng đầu
print('5 dòng đầu của dữ liệu:')
print(df.head())

# Thông tin cơ bản
print('\nThông tin dữ liệu:')
print(df.info())

# Kiểm tra số lượng giá trị thiếu
print('\nSố lượng giá trị thiếu ở từng cột:')
print(df.isna().sum())

# Nếu HoTen bị thiếu thì thay bằng "ChuaCapNhat"
df['HoTen'] = df['HoTen'].fillna('ChuaCapNhat')

# Nếu có chuỗi rỗng trong HoTen thì cũng thay
# ví dụ: "" hoặc khoảng trắng

df['HoTen'] = df['HoTen'].replace('', 'ChuaCapNhat')
df['HoTen'] = df['HoTen'].replace(' ', 'ChuaCapNhat')

# Tính trung bình của DiemQT và DiemThi
mean_diemqt = df['DiemQT'].mean()
mean_diemthi = df['DiemThi'].mean()

# Điền giá trị thiếu bằng trung bình cột
df['DiemQT'] = df['DiemQT'].fillna(mean_diemqt)
df['DiemThi'] = df['DiemThi'].fillna(mean_diemthi)

# Tính lại điểm tổng kết
# DiemTK = 0.4 * DiemQT + 0.6 * DiemThi

df['DiemTK'] = 0.4 * df['DiemQT'] + 0.6 * df['DiemThi']

# Làm tròn đến 2 chữ số thập phân

df['DiemTK'] = df['DiemTK'].round(2)

# Hàm xếp loại

def xep_loai(diem):
    if diem >= 8.5:
        return 'A'
    elif diem >= 7:
        return 'B'
    elif diem >= 5.5:
        return 'C'
    else:
        return 'D'

# Thêm cột XepLoai

df['XepLoai'] = df['DiemTK'].apply(xep_loai)

# Hiển thị dữ liệu sau khi xử lý
print('\nDữ liệu sau khi làm sạch:')
print(df)

# Kiểm tra lại xem còn thiếu dữ liệu không
print('\nSố lượng giá trị thiếu sau khi xử lý:')
print(df.isna().sum())

# Lưu ra file mới
output_file = 'diem_sinhvien_sau_xu_ly.csv'
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f'\nĐã lưu file sau xử lý vào: {output_file}')