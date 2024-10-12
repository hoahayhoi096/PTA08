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