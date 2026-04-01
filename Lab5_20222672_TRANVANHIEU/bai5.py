import numpy as np
import matplotlib.pyplot as plt

# Để kết quả luôn giống nhau mỗi lần chạy
np.random.seed(42)

# 1. Tạo 100 bước ngẫu nhiên (+1 hoặc -1)
steps = np.random.choice([-1, 1], size=100)

# 2. Tính vị trí sau mỗi bước
walk = np.cumsum(steps)

# 3. In 10 giá trị đầu tiên của dãy vị trí
print("10 vị trí đầu tiên:")
print(walk[:10])

# 5. In vị trí cuối cùng, lớn nhất và nhỏ nhất
print("\nVị trí cuối cùng:", walk[-1])
print("Vị trí lớn nhất:", np.max(walk))
print("Vị trí nhỏ nhất:", np.min(walk))

# 4. Vẽ đồ thị random walk
plt.figure(figsize=(10, 5))
plt.plot(walk)
plt.title("Random Walk 1 chiều")
plt.xlabel("Bước")
plt.ylabel("Vị trí")
plt.grid(True)
plt.show()

# =========================================
# PHẦN NÂNG CAO
# Mô phỏng 100 random walk, mỗi walk 100 bước
# =========================================

steps_many = np.random.choice([-1, 1], size=(100, 100))

# Tính vị trí của từng walk
walks_many = np.cumsum(steps_many, axis=1)

# Vị trí cuối cùng của mỗi walk
final_positions = walks_many[:, -1]

# Đếm số walk kết thúc ở vị trí dương
positive_walks = np.sum(final_positions > 0)
print("\nSố walk kết thúc dương:", positive_walks)

# Kiểm tra walk nào từng đạt |vị trí| >= 10
hit_10 = np.any(np.abs(walks_many) >= 10, axis=1)

# Đếm số walk chạm ngưỡng |10|
num_hit_10 = np.sum(hit_10)
print("Số walk chạm ngưỡng |10|:", num_hit_10)