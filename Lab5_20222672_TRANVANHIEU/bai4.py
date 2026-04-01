import numpy as np

# Khai báo hai ma trận
A = np.array([
    [2, 1],
    [1, 3]
])

B = np.array([
    [4, 2],
    [1, 5]
])

# 1. Tính A + B
print("1. A + B =")
print(A + B)

# 2. Tính A - B
print("\n2. A - B =")
print(A - B)

# 3. Tính tích ma trận A @ B
print("\n3. A @ B =")
print(A @ B)

# 4. Tính định thức của ma trận A
det_A = np.linalg.det(A)
print("\n4. det(A) =", det_A)

# 5. Tính ma trận nghịch đảo của A
if det_A != 0:
    inv_A = np.linalg.inv(A)
    print("\n5. Ma trận nghịch đảo của A:")
    print(inv_A)
else:
    print("\n5. A không có ma trận nghịch đảo vì det(A) = 0")

# 6. Giải hệ phương trình:
# 2x + y = 5
# x + 3y = 7

b = np.array([5, 7])

solution = np.linalg.solve(A, b)

print("\n6. Nghiệm của hệ phương trình:")
print("x =", solution[0])
print("y =", solution[1])

# ==========================
# PHẦN MỞ RỘNG
# Kiểm tra lại nghiệm
# ==========================

x, y = solution

eq1 = 2 * x + y
eq2 = x + 3 * y

print("\nKiểm tra lại nghiệm:")
print("2x + y =", eq1)
print("x + 3y =", eq2)

# Giải thích khi nào ma trận không khả nghịch
print("\nGiải thích:")
print("- Ma trận khả nghịch khi det(A) khác 0.")
print("- Nếu det(A) = 0 thì ma trận không khả nghịch.")
print("- Khi đó không thể tính A^-1 và hệ phương trình có thể vô số nghiệm hoặc vô nghiệm.")