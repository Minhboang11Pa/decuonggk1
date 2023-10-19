# Nhập số phiếu của từng đội
p = int(input("Nhập số phiếu của đội 1: "))
q = int(input("Nhập số phiếu của đội 2: "))
r = int(input("Nhập số phiếu của đội 3: "))

# Xác định đội nào đạt giải nhất hoặc có cùng số phiếu cao nhất
if p > q and p > r:
    print("Đội 1 đạt giải nhất.")
elif q > p and q > r:
    print("Đội 2 đạt giải nhất.")
elif r > p and r > q:
    print("Đội 3 đạt giải nhất.")
else:
    print("Bầu lại.")
