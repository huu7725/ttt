def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def la_cap_so_cong(danh_sach):
    if len(danh_sach) < 2:
        return True
    hieu = danh_sach[1] - danh_sach[0]
    for i in range(1, len(danh_sach)):
        if danh_sach[i] - danh_sach[i - 1] != hieu:
            return False
    return True

# Nhập danh sách các số nguyên
danh_sach = list(map(int, input("Nhập danh sách các số nguyên, cách nhau bởi dấu cách: ").split()))

# In ra các số chẵn trong danh sách
so_chan = [so for so in danh_sach if so % 2 == 0]
print("Các số chẵn trong danh sách:", so_chan)

# Nhập số nguyên X và đếm số lần xuất hiện, vị trí đầu tiên
X = int(input("Nhập số nguyên X: "))
so_lan_X = danh_sach.count(X)
if so_lan_X > 0:
    vi_tri_dau_X = danh_sach.index(X)
    print(f"Số {X} xuất hiện {so_lan_X} lần, vị trí đầu tiên: {vi_tri_dau_X}")
else:
    print(f"Số {X} không xuất hiện trong danh sách.")

# Tính tổng các số nguyên tố trong danh sách
tong_nguyen_to = sum(so for so in danh_sach if la_so_nguyen_to(so))
print("Tổng các số nguyên tố trong danh sách:", tong_nguyen_to)

# Kiểm tra danh sách có phải cấp số cộng không
if la_cap_so_cong(danh_sach):
    print("Danh sách tạo thành cấp số cộng.")
else:
    print("Danh sách không tạo thành cấp số cộng.")