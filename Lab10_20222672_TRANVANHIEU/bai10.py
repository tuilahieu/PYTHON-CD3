import pandas as pd
import numpy as np

# ===== 1. Đọc dữ liệu =====
df = pd.read_csv("student_performance_dirty.csv")

# ===== 2. Làm sạch dữ liệu (tóm tắt pipeline) =====

# Chuẩn hóa class_name
df["class_name"] = (
    df["class_name"]
    .str.replace("-", " ", regex=False)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
    .str.upper()
    .replace({
        "CNTT1": "CNTT 1",
        "CNTT2": "CNTT 2",
        "CNTT3": "CNTT 3"
    })
)

# Chuẩn hóa gender
df["gender"] = (
    df["gender"]
    .astype("string")
    .str.strip()
    .str.lower()
    .replace({
        "nam": "Nam",
        "nữ": "Nữ",
        "nu": "Nữ"
    })
    .fillna("Không rõ")
)

# Xử lý missing
df["attendance_rate"] = df["attendance_rate"].fillna(df["attendance_rate"].median())
df["phone"] = df["phone"].fillna("Chưa cập nhật")

# Xóa trùng
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["student_id"], keep="first")

# Xử lý điểm sai
invalid_score = ~df["score_python"].between(0, 10)
df.loc[invalid_score, "score_python"] = np.nan
df["score_python"] = df["score_python"].fillna(df["score_python"].median())

# Chuẩn hóa chuỗi
df["full_name"] = (
    df["full_name"]
    .astype("string")
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
    .str.title()
)

# Email
email_mask = df["email"].astype("string").str.contains(
    r"^[\w\.-]+@[\w\.-]+\.\w+$", regex=True, na=False
)
df.loc[~email_mask, "email"] = pd.NA

# Phone
df["phone"] = df["phone"].astype("string").str.replace(r"\D", "", regex=True)

# Datetime
df["birth_date"] = pd.to_datetime(df["birth_date"], errors="coerce", dayfirst=True)

# ===== 3. Lưu file =====
df.to_csv("student_performance_clean.csv", index=False, encoding="utf-8-sig")

print("Đã lưu file student_performance_clean.csv")