import numpy as np

a = np.array([2, 4, 6, 8, 10])
print('Mảng: ', a)

tong = np.sum(a)
print("Tổng các phần tử:", tong)

trung_binh = np.mean(a)
print("Giá trị trung bình:", trung_binh)

lon_nhat = np.max(a)
print("Phần tử lớn nhất:", lon_nhat)

nho_nhat = np.min(a)
print("Phần tử nhỏ nhất:", nho_nhat)