import numpy as np

# Số lượng bán được của 3 sản phẩm trong 4 ngày
quantity = np.array([
    [10, 12, 9, 14],
    [5, 7, 8, 6],
    [20, 18, 25, 22]
])

# Giá của từng sản phẩm
price = np.array([15000, 25000, 10000])

# 1. Tính doanh thu của từng sản phẩm theo từng ngày
# reshape(3,1) để biến price thành cột và broadcasting theo từng ngày
revenue = quantity * price.reshape(3, 1)

print("1. Doanh thu từng sản phẩm theo từng ngày:")
print(revenue)

# 2. Tính tổng doanh thu của từng sản phẩm
sum_product = np.sum(revenue, axis=1)

print("\n2. Tổng doanh thu từng sản phẩm:")
for i, total in enumerate(sum_product, start=1):
    print(f"Sản phẩm {i}: {total:,} đồng")

# 3. Tính tổng doanh thu của từng ngày
sum_day = np.sum(revenue, axis=0)

print("\n3. Tổng doanh thu từng ngày:")
for i, total in enumerate(sum_day, start=1):
    print(f"Ngày {i}: {total:,} đồng")

# 4. Tìm ngày có doanh thu cao nhất
best_day = np.argmax(sum_day) + 1

print(f"\n4. Ngày có doanh thu cao nhất: Ngày {best_day}")

# 5. Tính tỷ trọng doanh thu của từng sản phẩm
ratio = sum_product / np.sum(sum_product)

print("\n5. Tỷ trọng doanh thu của từng sản phẩm:")
for i, r in enumerate(ratio, start=1):
    print(f"Sản phẩm {i}: {r * 100:.2f}%")