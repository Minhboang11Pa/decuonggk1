# Nhập số nguyên dương N từ người dùng
N = int(input("Nhập một số nguyên dương N: "))

# Kiểm tra xem N có chia hết cho cả 2 và 5 không
if N % 2 == 0 and N % 5 == 0:
    print(f"{N} chia hết cho cả 2 và 5.")
else:
    print(f"{N} không chia hết cho cả 2 và 5.")
