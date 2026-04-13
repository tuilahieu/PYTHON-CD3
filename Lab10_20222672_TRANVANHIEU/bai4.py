import pandas as pd

# ===== 1. Đọc dữ liệu =====
df = pd.read_csv("student_performance_dirty.csv")

# ===== 2. Kiểm tra trùng =====

# Trùng toàn bộ dòng
print("=== Số dòng trùng hoàn toàn ===")
print(df.duplicated().sum())

# Trùng theo student_id
print("\n=== Số dòng trùng theo student_id ===")
print(df.duplicated(subset=["student_id"]).sum())

# ===== 3. Xem thử dòng bị trùng (debug) =====
print("\n=== Các dòng bị trùng ===")
print(df[df.duplicated(subset=["student_id"], keep=False)])

# ===== 4. Xóa trùng =====

# B1: Xóa trùng toàn bộ
df = df.drop_duplicates()

# B2: Xóa trùng theo student_id (giữ dòng đầu)
df = df.drop_duplicates(subset=["student_id"], keep="first")

# ===== 5. Kiểm tra lại =====
print("\n=== Sau khi xóa trùng ===")
print("Tổng số dòng:", len(df))

print("\nCheck lại trùng:")
print("Full duplicate:", df.duplicated().sum())
print("Duplicate student_id:", df.duplicated(subset=["student_id"]).sum())

# ===== 6. Xem dữ liệu =====
print("\n=== Data preview ===")
print(df)