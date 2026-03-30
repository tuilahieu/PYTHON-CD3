import numpy as np

stock = np.array([35, 8, 12, 5, 40, 18, 7, 22, 9, 15])
min_stock = np.array([20, 15, 15, 10, 25, 20, 12, 18, 12, 15])
price = np.array([30, 25, 28, 22, 35, 20, 18, 24, 19, 21])

need_import = np.maximum(min_stock - stock, 0)

print("Số lượng cần nhập thêm:")
for i, qty in enumerate(need_import, start=1):
    print(f"Mặt hàng {i}: {qty}")
    
cost = need_import * price

print("\nChi phí nhập từng mặt hàng:")
for i, c in enumerate(cost, start=1):
    print(f"Mặt hàng {i}: {c}")
    
total_cost = cost.sum()

print("\nTổng chi phí nhập hàng:", total_cost)

status = np.where(stock < min_stock, "Thiếu hàng", "Đủ hàng")

print("\nTrạng thái các mặt hàng:")
for i, s in enumerate(status, start=1):
    print(f"Mặt hàng {i}: {s}")
    
top3_shortage = np.argsort(need_import)[::-1][:3] + 1

print("\n3 mặt hàng thiếu nhiều nhất:")
print("Mặt hàng", top3_shortage)

limited_need = np.clip(need_import, 0, 20)

print("\nSố lượng nhập sau khi giới hạn:")
print(limited_need)

limited_total_cost = (limited_need * price).sum()

print("\nTổng chi phí sau khi giới hạn:", limited_total_cost)

num_shortage = np.sum(need_import > 0)

print("\nNhận xét:")
print(f"Có {num_shortage}/10 mặt hàng đang thiếu so với mức tối thiểu.")

if num_shortage >= 5:
    print("Kho đang thiếu khá nhiều mặt hàng, cần nhập bổ sung sớm.")
else:
    print("Kho chỉ thiếu một số mặt hàng, mức độ thiếu hụt chưa nghiêm trọng.")

print(
    f"Mặt hàng thiếu nhiều nhất là mặt hàng {top3_shortage[0]}, nên được ưu tiên nhập trước."
)
