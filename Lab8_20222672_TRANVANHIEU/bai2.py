import pandas as pd

# Đọc sai: pandas mặc định dùng dấu phẩy ,
df_sai = pd.read_csv("sales_semicolon.csv")

print(df_sai.head())
print(df_sai.columns)

# Đọc đúng: khai báo sep=';'
df_dung = pd.read_csv("sales_semicolon.csv", sep=";")

print("Đọc đúng:")
print(df_dung)
print("Kích thước:", df_dung.shape)
print("Tên cột:", df_dung.columns)