import numpy as np

sales = np.array([
    [120, 150, 130, 140, 160],
    [125, 145, 128, 142, 158],
    [130, 155, 135, 150, 162],
    [135, 160, 140, 152, 168],
    [140, 165, 145, 155, 170],
    [138, 162, 142, 153, 169],
    [145, 170, 150, 160, 175]
])

daily_total = sales.sum(axis=1)

print("Tổng doanh thu từng ngày:")
for i, total in enumerate(daily_total, start=1):
    print(f"Ngày {i}: {total}")

product_total = sales.sum(axis=0)
product_mean = sales.mean(axis=0)

print("\nTổng doanh thu từng sản phẩm:")
for i, total in enumerate(product_total, start=1):
    print(f"Sản phẩm {i}: {total}")

print("\nDoanh thu trung bình từng sản phẩm:")
for i, mean in enumerate(product_mean, start=1):
    print(f"Sản phẩm {i}: {mean:.2f}")

best_day = np.argmax(daily_total) + 1
best_product = np.argmax(product_total) + 1

print("\nNgày có doanh thu cao nhất: Ngày", best_day)
print("Sản phẩm bán tốt nhất toàn tuần: Sản phẩm", best_product)

new_sales = sales.astype(float).copy()
new_sales[:, [1, 4]] *= 1.08

print("\nDoanh thu sau điều chỉnh:")
print(np.round(new_sales, 2))

old_total = sales.sum()
new_total = new_sales.sum()

print("\nTổng doanh thu cũ:", old_total)
print("Tổng doanh thu mới:", round(new_total, 2))
print("Chênh lệch:", round(new_total - old_total, 2))

avg_daily_total = daily_total.mean()
good_days = np.where(daily_total > avg_daily_total)[0] + 1

print("\nDoanh thu trung bình mỗi ngày:", round(avg_daily_total, 2))
print("Các ngày có doanh thu lớn hơn trung bình:")
print("Ngày", good_days)

product_std = sales.std(axis=0)
stable_product = np.argmin(product_std) + 1

print("\nĐộ lệch chuẩn từng sản phẩm:")
for i, std in enumerate(product_std, start=1):
    print(f"Sản phẩm {i}: {std:.2f}")

print("Sản phẩm ổn định nhất: Sản phẩm", stable_product)

print("\nNhận xét:")
print(
    f"Sản phẩm {best_product} có tổng doanh thu cao nhất nên nên được ưu tiên bán."
)
print(
    f"Sản phẩm {stable_product} có doanh thu ổn định nhất, phù hợp để duy trì lâu dài."
)

if best_product == stable_product:
    print("Đây là sản phẩm vừa bán chạy vừa ổn định, rất đáng ưu tiên.")
else:
    print("Nên kết hợp ưu tiên sản phẩm bán chạy và duy trì sản phẩm ổn định.")
