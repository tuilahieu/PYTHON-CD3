import pandas as pd

# Đọc file không có tiêu đề cột
# header=None: báo cho pandas biết file không có header
# names=[...]: tự đặt tên cho các cột

df = pd.read_csv(
    "scores_no_header.csv",
    header=None,
    names=["MaSV", "HoTen", "Lop", "DiemQT", "DiemThi"]
)

# Hiển thị 5 dòng đầu
print(df.head())

# Hiển thị thông tin dữ liệu
print(df.info())