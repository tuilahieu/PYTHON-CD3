import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv("data.csv")

# Vẽ histogram cho điểm Final
df["Final"].plot(kind="hist", bins=10)

plt.title("Phan phoi diem Final")
plt.xlabel("Diem")
plt.ylabel("So luong sinh vien")

plt.show()