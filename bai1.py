# Nhập chiều dài đáy trên, đáy dưới và chiều cao từ người dùng
a = float(input("Nhập chiều dài đáy trên (a): "))
b = float(input("Nhập chiều dài đáy dưới (b): "))
h = float(input("Nhập chiều cao (h): "))

# Tính diện tích hình thang
dien_tich = (a + b) * h / 2

# In kết quả
print(f"Diện tích của hình thang có đáy trên {a}, đáy dưới {b}, và chiều cao {h} là: {dien_tich}")
