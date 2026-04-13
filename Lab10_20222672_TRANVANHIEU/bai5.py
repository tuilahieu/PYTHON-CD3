import pandas as pd
import numpy as np

# ===== 1. Đọc dữ liệu =====
df = pd.read_csv("student_performance_dirty.csv")

# ===== 2. Phát hiện điểm không hợp lệ =====
invalid_score = ~df["score_python"].between(0, 10)

print("=== Các giá trị điểm không hợp lệ ===")
print(df.loc[invalid_score, ["student_id", "score_python"]])

# ===== 3. Đánh dấu về NaN =====
df.loc[invalid_score, "score_python"] = np.nan

# ===== 4. Điền lại bằng median =====
median_score = df["score_python"].median()
df["score_python"] = df["score_python"].fillna(median_score)

# ===== 5. Kiểm tra lại =====
print("\n=== Sau khi xử lý ===")
print(df[["student_id", "score_python"]])

print("\nMin score:", df["score_python"].min())
print("Max score:", df["score_python"].max())