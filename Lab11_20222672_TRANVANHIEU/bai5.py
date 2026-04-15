import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv("data.csv")

# Vẽ scatter plot
df.plot(kind="scatter", x="StudyHours", y="Final")

plt.title("Moi quan he giua StudyHours va Final")
plt.xlabel("So gio hoc")
plt.ylabel("Diem Final")

plt.show()