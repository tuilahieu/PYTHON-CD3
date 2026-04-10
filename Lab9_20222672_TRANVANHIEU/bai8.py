import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("chitieu.csv")

# 1. Kiểm tra giao dịch không hợp lệ
invalid = df[df["SoTien"] <= 0]
print("Giao dịch không hợp lệ:")
print(invalid)

# 2. Loại bỏ dòng không hợp lệ
df = df[df["SoTien"] > 0]

# 3. Dùng cut() phân nhóm chi tiêu
df["MucChiTieu"] = pd.cut(
    df["SoTien"],
    bins=[0, 100000, 1000000, float("inf")],
    labels=["Thap", "TrungBinh", "Cao"]
)

# 4. Thống kê số giao dịch theo mức chi tiêu
print("\nSố giao dịch theo mức chi tiêu:")
print(df["MucChiTieu"].value_counts())

# 5. Tổng chi tiêu theo nhóm
tong_chi = df.groupby("NhomChiTieu")["SoTien"].agg(["count", "sum"])

print("\nTổng chi tiêu theo nhóm:")
print(tong_chi)

# Kết quả cuối
print("\nDữ liệu sau xử lý:")
print(df)