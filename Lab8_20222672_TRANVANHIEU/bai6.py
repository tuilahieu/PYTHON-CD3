import pandas as pd

# Đọc file Excel, sheet HangHoa
df = pd.read_excel(
    "inventory.xlsx",
    sheet_name="HangHoa"
)

# Hiển thị 10 dòng đầu
print("10 dòng đầu tiên:")
print(df.head(10))

# Lọc các mặt hàng có tồn kho dưới 20
hang_sap_het = df[df["SoLuongTon"] < 20]

# Hiển thị kết quả
print("\nCác mặt hàng có tồn kho dưới 20:")
print(hang_sap_het)