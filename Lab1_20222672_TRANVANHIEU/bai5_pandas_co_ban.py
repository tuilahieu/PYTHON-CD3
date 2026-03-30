import pandas as pd
data = {
"MaSV": ["SV01", "SV02", "SV03"],
"HoTen": ["Nguyen Van A", "Tran Thi B", "Le Van C"],
"Lop": ["CNTT1", "CNTT1", "CNTT2"],
"Diem": [8.0, 7.5, 9.0]
}
df = pd.DataFrame(data)
print(df)

print("\n2 dòng đầu tiên:")
print(df.head(2))

print("\nTên các cột:")
print(df.columns)

diem_tb = df["Diem"].mean()
print("\nĐiểm trung bình:", diem_tb)