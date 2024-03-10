#buat modul bangun datar (min 7)

import math

def luas_persegi(sisi):
    return sisi ** 2

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

def keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def luas_trapesium(alas_atas, alas_bawah, tinggi):
    return 0.5 * (alas_atas + alas_bawah) * tinggi

def keliling_trapesium(sisi1, sisi2, sisi3, sisi4):
    return sisi1 + sisi2 + sisi3 + sisi4

def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

def keliling_jajar_genjang(sisi1, sisi2):
    return 2 * (sisi1 + sisi2)

def luas_belahketupat(bil1, bil2):
    luas = 0.5 * bil1 * bil2
    print(f"Luas belah ketupat: {luas}")

def keliling_belahketupat(bil1, bil2):
    keliling = 4 * (bil1 ** 2 + bil2 ** 2) ** 0.5
    print(f"Keliling belah ketupat: {keliling}")