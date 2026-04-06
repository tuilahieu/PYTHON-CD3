from bai1 import df

df["DiemTB"] = (
    0.2 * df["DiemQT"]
    + 0.3 * df["DiemGK"]
    + 0.5 * df["DiemCK"]
)

print(df[["MaSV", "HoTen", "DiemTB"]])   