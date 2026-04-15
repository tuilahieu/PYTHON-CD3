import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv("data.csv")

# Nhóm theo Gender và tính trung bình điểm Final
group_data = df.groupby("Gender")["Final"].mean()

# In ra để kiểm tra
print(group_data)

# Vẽ biểu đồ cột
group_data.plot(kind="bar")

plt.title("Diem Final trung binh theo gioi tinh")
plt.xlabel("Gioi tinh")
plt.ylabel("Diem Final trung binh")

plt.show()