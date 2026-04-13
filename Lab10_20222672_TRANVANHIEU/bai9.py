import pandas as pd

# ===== 1. Đọc dữ liệu =====
df = pd.read_csv("student_performance_dirty.csv")

# ===== 2. (NÊN CÓ) xử lý missing trước =====
median_attendance = df["attendance_rate"].median()
df["attendance_rate"] = df["attendance_rate"].fillna(median_attendance)

# ===== 3. Tính IQR =====
q1 = df["attendance_rate"].quantile(0.25)
q3 = df["attendance_rate"].quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower bound:", lower)
print("Upper bound:", upper)

# ===== 4. Lọc outlier =====
outlier_df = df[
    (df["attendance_rate"] < lower) |
    (df["attendance_rate"] > upper)
]

print("\n=== Các bản ghi bất thường ===")
print(outlier_df[["student_id", "attendance_rate"]])

# ===== 5. Lưu danh sách nghi ngờ =====
outlier_df.to_csv("attendance_outliers.csv", index=False, encoding="utf-8-sig")

print("\nĐã lưu file attendance_outliers.csv")