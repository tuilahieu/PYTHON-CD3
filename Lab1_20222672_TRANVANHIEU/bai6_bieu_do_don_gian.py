import matplotlib.pyplot as plt

# 1. Danh sách tên sinh viên
ten = ["Nguyễn Văn A", "Trần Thị B", "Lê Văn C", "Phạm Văn D", "Hoàng Thị E"]

# 2. Danh sách điểm
diem = [8, 7, 9, 6, 8.5]

# 3. Vẽ biểu đồ cột
plt.bar(ten, diem)

# 4. Tiêu đề
plt.title("Điểm của sinh viên")

# 5. Tên trục
plt.xlabel("Sinh viên")
plt.ylabel("Điểm")

# (Tuỳ chọn) xoay tên cho dễ nhìn
plt.xticks(rotation=30)

# 6. Hiển thị
plt.show()