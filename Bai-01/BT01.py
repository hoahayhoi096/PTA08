# name = 10 
# print(name)

# hoVaTen = input("What's your name: ")

# Câu lệnh rẽ nhánh 
# a = int(input("Mời bạn nhập một số vào: "))
# if a < 10: 
#     print("Số bạn nhập vào nhỏ hơn 10!")
# elif a == 10: 
#     print("Số bạn nhập vào bằng 10!")
# else:
#     print("Số bạn nhập vào lớn hơn 10!")

# Sử dụng vòng lặp 
# Tong = 0 
# for i in range(1, 1000): 
#     Tong += i
# print(Tong)


# Sử dụng danh sách 
# a = [1, 2, 3, 4, 5]

# print(a[0])

# for i in range(0,len(a)): 
#     print(a[i])

# Lấy ví dụ xâu chuỗi 
# xau = "Hello"
# for i in range(0, len(xau)):
#     kitu = xau[i]
#     print(kitu)

# Sử dụng hàm 
# Hàm không có giá trị trả về 
def Hello():
    print("Xin chào tôi là Mindx")
    print("Rất vui được gặp bạn")

Hello()

# Hàm có giá trị trả về 
# def HDT1():
#     ( a + b ) = a**2 + 2 * a * b + b ** 2
#     return 

# def KiemTraGiac(a, b, c):
#     x, y, z = sorted([a, b, c])
#     if x == y == z: 
#         return "Tam giác đều!" # Tam giác đều 
#     elif x == y or y == z:
#         return "Tam giác cân" # Tam giác cân 
    
# a = int(input("Nhập vào a: "))
# b = int(input("Nhập vào b: "))
# c = int(input("Nhập vào c: "))
# A = KiemTraGiac(a, b ,c)
# print(A)

# Viết hàm sử dụng vòng lặp để nhập các phần tử vào một danh sách 
#   (danh sách này ban đầu là ds rỗng)
# sau đó loại bỏ các số chẵn trong danh sách và in ra màn hình

# hàm có thêm vào danh sách có sẵn: append(), remove()
# n = int(input("Nhập vào số phần tử của danh sách: "))
# for i in range(0, n):
    # Lệnh nhập vào danh sách: .... 
def nhap_danh_sach():
    danh_sach = []
    so_luong = int(input("Nhập số lượng phần tử trong danh sách: "))
    
    for i in range(so_luong):
        phan_tu = int(input("Phần tử: "))
        danh_sach.append(phan_tu)

    # Loại bỏ số chẵn trong danh sách
    for phan_tu in danh_sach[:]:  # Sử dụng danh sách sao chép để tránh lỗi khi thay đổi danh sách
        if phan_tu % 2 == 0:
            danh_sach.remove(phan_tu)

    return danh_sach

# Gọi hàm và in ra danh sách
danh_sach_ket_qua = nhap_danh_sach()
print("Danh sách đã nhập (sau khi loại bỏ số chẵn):", danh_sach_ket_qua)



