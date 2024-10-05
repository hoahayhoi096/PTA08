class Xe:
    def __init__(self, loai, ten, soChoNgoi):
        self.loai = loai
        self.ten = ten
        self.soChoNgoi = soChoNgoi

    def ThongTin(self):
        print("Loại:", self.loai)
        print("Tên:", self.ten)
        print("Số chỗ ngồi:", self.soChoNgoi)
