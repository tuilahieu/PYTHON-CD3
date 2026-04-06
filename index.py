import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =========================
# 1. Đọc dữ liệu
# =========================

df = pd.read_csv("store_customers.csv")

print("5 dòng đầu tiên:")
print(df.head())

print("\nThông tin dữ liệu:")
print(df.info())

print("\nSố lượng missing value:")
print(df.isnull().sum())

# =========================
# 2. Xử lý missing data
# =========================

# Điền tuổi bằng giá trị trung bình
age_imputer = SimpleImputer(strategy="mean")
df[["Age"]] = age_imputer.fit_transform(df[["Age"]])

# Điền thu nhập bằng trung vị
income_imputer = SimpleImputer(strategy="median")
df[["Annual Income (k$)"]] = income_imputer.fit_transform(
    df[["Annual Income (k$)"]]
)

# Điền Spending Score bằng trung bình
score_imputer = SimpleImputer(strategy="mean")
df[["Spending Score (1-100)"]] = score_imputer.fit_transform(
    df[["Spending Score (1-100)"]]
)

print("\nSau khi xử lý missing:")
print(df.isnull().sum())

# =========================
# 3. Phân nhóm khách hàng theo độ tuổi
# =========================

def age_group(age):
    if age < 25:
        return "<25"
    elif age < 35:
        return "25-34"
    elif age < 45:
        return "35-44"
    else:
        return "45+"


df["Age Group"] = df["Age"].apply(age_group)

# =========================
# 4. Phân nhóm khách hàng theo thu nhập
# =========================

def income_group(income):
    if income < 40:
        return "Thấp"
    elif income < 70:
        return "Trung bình"
    else:
        return "Cao"


df["Income Group"] = df["Annual Income (k$)"].apply(income_group)

print("\nPhân nhóm khách hàng:")
print(df[["CustomerID", "Age Group", "Income Group"]].head(10))

# =========================
# 5. Phân tích hành vi mua hàng
# =========================

behavior = df.groupby("Income Group")[["Spending Score (1-100)"]].mean()

print("\nChi tiêu trung bình theo nhóm thu nhập:")
print(behavior)

behavior_age = df.groupby("Age Group")[["Spending Score (1-100)"]].mean()

print("\nChi tiêu trung bình theo nhóm tuổi:")
print(behavior_age)

# =========================
# 6. Trực quan hóa dữ liệu
# =========================

# Phân bố độ tuổi
plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=10, edgecolor="black")
plt.title("Phân bố độ tuổi khách hàng")
plt.xlabel("Tuổi")
plt.ylabel("Số lượng")
plt.show()

# Phân bố nhóm thu nhập
plt.figure(figsize=(8,5))
df["Income Group"].value_counts().plot(kind="bar")
plt.title("Số lượng khách hàng theo nhóm thu nhập")
plt.xlabel("Nhóm thu nhập")
plt.ylabel("Số lượng")
plt.show()

# Thu nhập và chi tiêu
plt.figure(figsize=(8,5))
plt.scatter(
    df["Annual Income (k$)"],
    df["Spending Score (1-100)"],
    alpha=0.7
)
plt.title("Thu nhập và mức chi tiêu")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.show()

# Tuổi và chi tiêu
plt.figure(figsize=(8,5))
plt.scatter(
    df["Age"],
    df["Spending Score (1-100)"],
    alpha=0.7
)
plt.title("Độ tuổi và mức chi tiêu")
plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.show()

# =========================
# 7. Xây dựng mô hình dự đoán chi tiêu
# =========================

# Chuyển giới tính sang số
encoder = LabelEncoder()
df["Gender"] = encoder.fit_transform(df["Gender"])

# Biến đầu vào
X = df[["Gender", "Age", "Annual Income (k$)"]]

# Biến mục tiêu
y = df["Spending Score (1-100)"]

# Chia dữ liệu train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Huấn luyện mô hình
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Dự đoán
predictions = model.predict(X_test)

# Đánh giá
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("\nKết quả đánh giá mô hình:")
print("MAE =", round(mae, 2))
print("RMSE =", round(rmse, 2))
print("R2 =", round(r2, 2))

# =========================
# 8. Dự đoán cho khách hàng mới
# =========================

# Nam = 1, Nữ = 0
new_customer = pd.DataFrame({
    "Gender": [1],
    "Age": [30],
    "Annual Income (k$)": [60]
})

predicted_score = model.predict(new_customer)

print("\nMức chi tiêu dự đoán của khách hàng mới:")
print(round(predicted_score[0], 2))