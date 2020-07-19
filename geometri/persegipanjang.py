# setelah class harus hurus Besar dan kata berbedanya huruf besar lagi

# harus buat class dulu baru objek
# objek adalah nama manusia yaitu a dan b
# manusia adalah class

# class itu adalah type data
# objek adalah variabelnya
from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        # fungsi yang dipanggil pertama kali saat object diciptakan
        self.p = p
        self.l = l
    def info(self):
        return f'Ini adalah object dari Persegi panjang dengan panjang = {self.p} dan lebar = {self.l}'

    def hitung_luas(self):
        return self.p * self.l