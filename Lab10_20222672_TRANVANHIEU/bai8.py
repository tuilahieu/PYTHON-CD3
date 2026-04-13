import pandas as pd

# ===== 1. Đọc dữ liệu =====
df = pd.read_csv("student_performance_dirty.csv")

# ===== 2. Tạo bins và labels =====
bins = [0, 5, 6.5, 8, 10]
labels = ["Yếu", "Trung bình", "Khá", "Giỏi"]

# ===== 3. Phân nhóm =====
df["level"] = pd.cut(
    df["score_python"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# ===== 4. Kiểm tra =====
print("=== Data preview ===")
print(df[["student_id", "score_python", "level"]])

# ===== 5. Thống kê số lượng mỗi nhóm =====
print("\n=== Thống kê level ===")
print(df["level"].value_counts())