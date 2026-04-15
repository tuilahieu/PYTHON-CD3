import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Đọc dữ liệu
df = pd.read_csv("data.csv")

# Chọn biến
X = df[["StudyHours"]]
y = df["Final"]

# Chia train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Tạo và huấn luyện model
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# Đánh giá
print("MSE:", mean_squared_error(y_test, y_pred))
print("He so (coef):", model.coef_)
print("Intercept:", model.intercept_)