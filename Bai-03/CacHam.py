# Hàm nhập vào danh sách các học sinh 
from fileClass1 import HocSinh
from fileclass2 import Xe

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


def nhap_danh_sach_xe():
    danh_sach_xe = []
    so_luong = int(input("Nhập số lượng xe trong danh sách: "))
    
    for i in range(so_luong):
        loai = input("Nhập vào loại: ")
        ten = input("Nhập vào tên xe: ")
        soChoNgoi = input("Nhập vào số chỗ ngồi: ")

        xe = Xe( loai, ten, soChoNgoi)
        danh_sach_xe.append(xe)
        
    return danh_sach_xe

def in_danh_sach_xe(ds):
    for i in range(0, len(ds)):
        ds[i].ThongTin()