import numpy as np

# Ma trận điểm của 5 sinh viên, mỗi hàng là 1 sinh viên
scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

# 1. In ra ma trận điểm
print("Ma trận điểm:")
print(scores)

# 2. Tính điểm trung bình của toàn bộ ma trận
avg_all = np.mean(scores)
print("\nĐiểm trung bình toàn bộ ma trận:", avg_all)

# 3. Tính điểm trung bình theo từng sinh viên
avg_students = np.mean(scores, axis=1)
print("\nĐiểm trung bình từng sinh viên:")
for i, avg in enumerate(avg_students, start=1):
    print(f"Sinh viên {i}: {avg:.2f}")

# 4. Tính điểm trung bình theo từng môn
avg_subjects = np.mean(scores, axis=0)
print("\nĐiểm trung bình từng môn:")
for i, avg in enumerate(avg_subjects, start=1):
    print(f"Môn {i}: {avg:.2f}")

# 5. Tìm điểm cao nhất và thấp nhất trong ma trận
max_score = np.max(scores)
min_score = np.min(scores)

print("\nĐiểm cao nhất:", max_score)
print("Điểm thấp nhất:", min_score)

# 6. Tính độ lệch chuẩn theo từng môn
std_subjects = np.std(scores, axis=0)
print("\nĐộ lệch chuẩn từng môn:")
for i, std in enumerate(std_subjects, start=1):
    print(f"Môn {i}: {std:.2f}")

# 7. Xác định sinh viên có điểm trung bình cao nhất
best_student = np.argmax(avg_students)

print(f"\nSinh viên có điểm trung bình cao nhất là sinh viên {best_student + 1}")
print(f"Điểm trung bình của sinh viên này: {avg_students[best_student]:.2f}")