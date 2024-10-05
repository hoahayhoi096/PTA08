# Hàm nhập vào danh sách các học sinh 
from fileClass1 import HocSinh

def nhap_danh_sach():
    danh_sach_hoc_sinh = []
    so_luong = int(input("Nhập số lượng học sinh trong danh sách: "))
    
    for i in range(so_luong):
        hocSinh = HocSinh()
        hocSinh.ten = input("Nhập vào tên: ")
        hocSinh.tuoi = int(input("Nhập vào tuổi: "))
        danh_sach_hoc_sinh.append(hocSinh)

    return danh_sach_hoc_sinh

def in_danh_sach(ds):
    for i in range(0, len(ds)):
        print("Học sinh thứ", i + 1)
        print("Tên: ", ds[i].ten)
        print("Tuổi: ", ds[i].tuoi)
