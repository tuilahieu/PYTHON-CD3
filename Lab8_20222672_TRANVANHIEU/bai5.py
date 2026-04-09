import pandas as pd

# File UTF-8
try:
    df1 = pd.read_csv("sinhvien_utf8.csv", encoding="utf-8")
    print("Đọc thành công sinhvien_utf8.csv")
    print(df1.head())
except Exception as e:
    print("Lỗi khi đọc UTF-8:", e)

print("-" * 40)

# # File ANSI
# try:
#     df2 = pd.read_csv("sinhvien_ansi.csv", encoding="cp1258")
#     print("Đọc thành công sinhvien_ansi.csv")
#     print(df2.head())
# except Exception as e:
#     print("Lỗi khi đọc ANSI:", e)