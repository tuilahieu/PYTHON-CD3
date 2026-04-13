import pandas as pd

# ===== 1. Đọc dữ liệu =====
df = pd.read_csv("student_performance_dirty.csv")

# ===== 2. Chuyển kiểu datetime =====
df["birth_date"] = pd.to_datetime(
    df["birth_date"],
    errors="coerce",   # lỗi → NaT
    dayfirst=True      # format dd-mm-yyyy
)

# ===== 3. Kiểm tra lỗi =====
print("=== Số giá trị không chuyển được ===")
print(df["birth_date"].isna().sum())

print("\n=== Các dòng lỗi ===")
print(df[df["birth_date"].isna()][["student_id", "birth_date"]])

# ===== 4. Kiểm tra kiểu dữ liệu =====
print("\n=== Kiểu dữ liệu ===")
print(df["birth_date"].dtype)

# ===== 5. Preview =====
print("\n=== Data preview ===")
print(df[["student_id", "birth_date"]])