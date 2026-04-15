import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv("data.csv")

# Vẽ boxplot
df.boxplot(column="Final")

plt.title("Boxplot phat hien ngoai le (Final)")
plt.ylabel("Diem Final")

plt.show()