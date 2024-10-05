class ConNguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi


class HocSinh(ConNguoi):
    def __init__(self, lopHoc, soThich):
        super().__init__(ten, tuoi)
        self.lopHoc = lopHoc
        self.soThich = soThich
        
    def ThongTin(self):
        print("Tên:", self.ten)
        print("Tuổi:", self.tuoi)

class GiaoVien(ConNguoi): 
    def __init__(self, luongCoban, hocVan):
        self.luongCoban = luongCoban
        self.hocVan = hocVan




