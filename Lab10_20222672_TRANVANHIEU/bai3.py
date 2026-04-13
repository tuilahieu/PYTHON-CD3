import pandas as pd

# ===== 1. Đọc dữ liệu =====
df = pd.read_csv("student_performance_dirty.csv")

# ===== 2. Xử lý giá trị thiếu =====

# Gender → "Không rõ"
df["gender"] = df["gender"].fillna("Không rõ")

# Attendance_rate → median
median_attendance = df["attendance_rate"].median()
df["attendance_rate"] = df["attendance_rate"].fillna(median_attendance)

# Phone → "Chưa cập nhật"
df["phone"] = df["phone"].fillna("Chưa cập nhật")

# ===== 3. Kiểm tra =====
print("=== Missing sau khi xử lý ===")
print(df.isna().sum())

print("\n=== Dữ liệu sau khi xử lý ===")
print(df[["student_id", "gender", "attendance_rate", "phone"]])