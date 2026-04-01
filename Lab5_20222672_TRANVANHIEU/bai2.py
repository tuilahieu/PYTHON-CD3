import numpy as np

# Ma trận điểm
scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

# 1. Tính vector trung bình từng môn
mean_col = np.mean(scores, axis=0)
print("Trung bình từng môn:")
print(mean_col)

# 2. Tính vector độ lệch chuẩn từng môn
std_col = np.std(scores, axis=0)
print("\nĐộ lệch chuẩn từng môn:")
print(std_col)

# 3. Chuẩn hóa toàn bộ ma trận bằng Z-score
z_scores = (scores - mean_col) / std_col

# 4. In ma trận đã chuẩn hóa, làm tròn 2 chữ số thập phân
print("\nMa trận sau khi chuẩn hóa Z-score:")
print(np.round(z_scores, 2))

# 5. Kiểm tra trung bình các cột sau chuẩn hóa
print("\nTrung bình các cột sau chuẩn hóa:")
print(np.round(np.mean(z_scores, axis=0), 10))

# =========================
# PHẦN MỞ RỘNG: Chuẩn hóa về [0, 1]
# =========================

# Tìm giá trị nhỏ nhất và lớn nhất của từng môn
min_col = np.min(scores, axis=0)
max_col = np.max(scores, axis=0)

# Chuẩn hóa Min-Max về khoảng [0, 1]
minmax_scores = (scores - min_col) / (max_col - min_col)

print("\nMa trận sau khi chuẩn hóa Min-Max [0, 1]:")
print(np.round(minmax_scores, 2))