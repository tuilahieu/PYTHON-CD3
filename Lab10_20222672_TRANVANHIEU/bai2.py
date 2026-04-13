import pandas as pd

# Đọc lại dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# ===== 1. Chuẩn hóa class_name =====
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

# ===== 2. Chuẩn hóa gender =====
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
)

# ===== 3. Kiểm tra kết quả =====
print("\n=== CLASS NAME UNIQUE ===")
print(df["class_name"].unique())

print("\n=== GENDER UNIQUE ===")
print(df["gender"].unique())

print("\n=== DATA PREVIEW ===")
print(df[["student_id", "class_name", "gender"]].head(10))