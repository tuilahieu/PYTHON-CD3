import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("moitruong.csv").copy()

# 🔥 FIX 1: ép kiểu FLOAT ngay từ đầu (QUAN TRỌNG NHẤT)
df["NhietDo"] = pd.to_numeric(df["NhietDo"], errors="coerce").astype(float)

# IQR
Q1 = df["NhietDo"].quantile(0.25)
Q3 = df["NhietDo"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Outlier
df["Outlier"] = (df["NhietDo"] < lower) | (df["NhietDo"] > upper)

print("Outlier:")
print(df[df["Outlier"]])

# median (ép float luôn)
median_temp = float(df["NhietDo"].median())

# 🔥 FIX 2: dùng .loc nhưng đảm bảo dtype float
df.loc[df["Outlier"], "NhietDo"] = median_temp

# kiểm tra
print("\nSau xử lý:")
print(df)

# boxplot
plt.boxplot(df["NhietDo"])
plt.title("NhietDo sau xử lý")
plt.show()