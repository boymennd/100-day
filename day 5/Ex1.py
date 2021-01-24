danh_sach = input("nhập danh sách điểm của học sinh:").split()
for n in range(0, len(danh_sach)):
    danh_sach[n] = int(danh_sach[n])
max=0
for a in danh_sach:
    if a > max :
        max = a
print(f"điêm cao nhất:{max}")
min=10
for b in danh_sach:
    if min > b:
        min = b
print(f"điểm thấp nhất:{min}")
tong_diem = 0
for diem in danh_sach:
    tong_diem += diem
print(tong_diem)
tong_hoc_sinh = 0
for hoc_sinh in danh_sach:
    tong_hoc_sinh += 1
print(tong_hoc_sinh)
trung_binh = round(tong_diem/ tong_hoc_sinh)
print(f"Điểm trung bình của {tong_hoc_sinh} học sinh là: {trung_binh}")