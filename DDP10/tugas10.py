### nama siswa yang lulus
'''Buat fungsi untuk menampilkan nama2 siswa yang lulus
saja dari hasil_akhir di slide sebelumnya (nilai > 65)'''

hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]
lulus_saja = [nama['nama'] for nama in hasil_akhir if nama['nilai'] > 65]
print("Siswa yang lulus:",lulus_saja)

### no 1
'''Buat fungsi untuk membuat list baru berisi urutan terbalik dari buah2an
menggunakan for dan materi yang sudah diajarkan. (tidak boleh pakai
fungsi dari python)'''

# Contoh penggunaan tanpa fungsi
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

# Buat list baru dengan urutan terbalik
listerbalik = []
for i in range(len(buah) - 1, -1, -1):
    listerbalik.append(buah[i])

# Tampilkan hasil
print("List Buah Asli:", buah)
print("List dengan Urutan Terbalik:", listerbalik)


### no 2
'''Buat fungsi untuk membuat list baru berisi isi list buah2an tetapi
terduplikasi'''

# Contoh penggunaan tanpa fungsi
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

# Buat list baru dengan elemen terduplikasi
listduplikat = []
for buah in buah:
    listduplikat.extend([buah, buah])

# Tampilkan hasil
print("List dengan Duplikasi:", listduplikat)

### no 3
'''Buat fungsi untuk membuat string baru berisi hanya konsonan dari string
fungsi(“Nurul Fikri”) Hasilnya: "NrlFkr"'''

vokal = "aiueo"
kalimat = "Nurul Fikri"
hasil = ""
for huruf in kalimat:
    if huruf.lower() not in vokal:
        hasil += huruf
print(hasil)