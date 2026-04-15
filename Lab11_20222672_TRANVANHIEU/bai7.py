import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Đọc dữ liệu
df = pd.read_csv("data.csv")

# Chuyển nhãn Pass/Fail -> 1/0
df["Result"] = df["Result"].map({"Fail": 0, "Pass": 1})

# Chọn biến đầu vào và đầu ra
X = df[["StudyHours", "Attendance", "Midterm", "Final", "Project"]]
y = df["Result"]

# Chia train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Tạo model
model = LogisticRegression(max_iter=1000)

# Huấn luyện
model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# Đánh giá
print("Accuracy:", accuracy_score(y_test, y_pred))