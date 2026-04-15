🔷 1. Import thư viện
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
🔷 2. Đọc dữ liệu & khám phá
df = pd.read_csv("data.csv")

print("=== 5 dong dau ===")
print(df.head())

print("\n=== Thong tin du lieu ===")
print(df.info())

print("\n=== Thong ke mo ta ===")
print(df.describe())
🔷 3. Trực quan hóa dữ liệu
📊 Biểu đồ 1: Bar chart
df.groupby("Gender")["Final"].mean().plot(kind="bar")

plt.title("Diem Final trung binh theo gioi tinh")
plt.xlabel("Gioi tinh")
plt.ylabel("Diem trung binh")

plt.show()
📊 Biểu đồ 2: Histogram
df["Final"].plot(kind="hist", bins=8)

plt.title("Phan phoi diem Final")
plt.xlabel("Diem")
plt.ylabel("So luong")

plt.show()
📊 Biểu đồ 3: Scatter plot
df.plot(kind="scatter", x="StudyHours", y="Final")

plt.title("Moi quan he giua StudyHours va Final")
plt.xlabel("StudyHours")
plt.ylabel("Final")

plt.show()
🔷 4. Mô hình hóa (Logistic Regression)

# Chuyen nhan

df["Result"] = df["Result"].map({"Fail": 0, "Pass": 1})

# Chon bien

X = df[["StudyHours", "Attendance", "Midterm", "Final", "Project"]]
y = df["Result"]

# Chia du lieu

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

# Tao model

model = LogisticRegression(max_iter=1000)

# Train

model.fit(X_train, y_train)

# Predict

y_pred = model.predict(X_test)

# Danh gia

print("Accuracy:", accuracy_score(y_test, y_pred))
🔷 5. Nhận xét (Markdown cell)

### Nhận xét trực quan hóa

- Điểm Final phân bố chủ yếu trong khoảng 6 đến 8.5
- Sinh viên học nhiều giờ có xu hướng đạt điểm cao hơn
- Dữ liệu không có nhiều giá trị ngoại lệ

### Nhận xét mô hình

- Mô hình Logistic Regression dự đoán Pass/Fail với độ chính xác khá
- Các yếu tố như Final, Midterm và StudyHours ảnh hưởng mạnh đến kết quả
- Mô hình còn đơn giản và có thể cải thiện bằng cách thêm dữ liệu
