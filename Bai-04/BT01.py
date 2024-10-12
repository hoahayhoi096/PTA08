class DongVat:
    def __init__(self, ten, tuoi, loai, moiTruongSong):
        self.ten = ten
        self.tuoi = tuoi
        self.loai = loai
        self.moiTruongSong = moiTruongSong

    def capNhatMoiTruong(self, moiTruongSongMoi):
        self.moiTruongSong = moiTruongSongMoi

    def thongTin(self):
        print("Tên: ", self.ten)
        print("Tuổi: ", self.tuoi)
        print("Loài: ", self.loai)
        print("Môi trường sống: ", self.moiTruongSong)

kitty = DongVat("Kitty", 1, "Mèo", "Trên cạn")
kitty.thongTin()

kitty.capNhatMoiTruong("Dưới nước")
kitty.thongTin()



# Bài 2 
class PhuongTien:
    def __init__(self, bien_so, hang_xe, mau_sac):
        self.bien_so = bien_so
        self.hang_xe = hang_xe
        self.mau_sac = mau_sac

    def capNhatMauSac(self, mauSacMoi):
        self.mau_sac = mauSacMoi

    def thongTin(self):
        print("Biển sô: ", self.bien_so)
        print("Hãn xe: ", self.hang_xe)
        print("Màu sắc: ", self.mau_sac)


class XeMay(PhuongTien):
    def __init__(self, bien_so, hang_xe, mau_sac, loai_xe):
        super().__init__(bien_so, hang_xe, mau_sac)
        self.loai_xe = loai_xe

    def display_info(self):
        self.thongTin()
        print("Loại xe: ", self.loai_xe)


class Oto(PhuongTien):
    def __init__(self, bien_so, hang_xe, mau_sac, soChoNgoi):
        super().__init__(bien_so, hang_xe, mau_sac)
        self.so_cho_ngoi = soChoNgoi

    def display_info(self):
        self.thongTin()
        print("Số chỗ ngồi: ", self.so_cho_ngoi)

xeMay1 = XeMay("47AB 20017", "Yamaha", "Hồng", "Tay ga")
xeMay1.display_info()
