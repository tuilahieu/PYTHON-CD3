import pandas as pd

df = pd.read_csv("diem_sinhvien.csv")

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())