from geometri.bangun_ruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('Menggunakan OOP')
# p1 adalah objek, PersegiPanjang adalah classnya
p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(10, 4)
print(s1.info())
print(s1.hitung_luas())

### Inheritance, pewarisan sifat dari class yang berbeda, BangunRuang adalah yang tertinggi bisa kita bilang ayahnya###
# PersegiPanjang dan Segitiga adalah anak dari BangunRuang memiliki 2 sifat yang sama yaitu info dan hitung_luas,

print('\nMencoba membuat object dari kelas BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

### Polymorphism adalah 2 class manusia dan kuda adalah anak dari class mamalia, akan bisa tau anak mamalia akan bicara
## tapi impelementasi berbeda, itu Polymorphism
## Polymorphism: kemampuan objek untuk merespon berbeda terhadap pemanggilan method yang sama ##

daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\nPolymorphism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())