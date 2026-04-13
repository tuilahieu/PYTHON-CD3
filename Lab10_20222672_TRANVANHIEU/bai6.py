import pandas as pd

# ===== 1. Đọc dữ liệu =====
df = pd.read_csv("student_performance_dirty.csv")

# ===== 2. Chuẩn hóa full_name =====
df["full_name"] = (
    df["full_name"]
    .astype("string")
    .str.replace(r"\s+", " ", regex=True)  # nhiều space -> 1
    .str.strip()                           # xóa space đầu/cuối
    .str.title()                           # Viết Hoa Mỗi Chữ
)

# ===== 3. Kiểm tra email sai =====
email_mask = df["email"].astype("string").str.contains(
    r"^[\w\.-]+@[\w\.-]+\.\w+$", regex=True, na=False
)

print("=== Email không hợp lệ ===")
print(df.loc[~email_mask, ["student_id", "email"]])

# (Không bắt buộc nhưng nên làm) → đánh dấu email lỗi = NaN
df.loc[~email_mask, "email"] = pd.NA

# ===== 4. Chuẩn hóa phone =====
df["phone"] = (
    df["phone"]
    .astype("string")
    .str.replace(r"\D", "", regex=True)  # xóa tất cả ký tự không phải số
)

# ===== 5. Kiểm tra kết quả =====
print("\n=== Data sau khi chuẩn hóa ===")
print(df[["student_id", "full_name", "email", "phone"]])