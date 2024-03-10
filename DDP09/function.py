#deklarasi fungsi
def hello_world():
    print("hello saya dalah STT Teradu Nurul Fikri")
    print("saya program studi teknik informatika")

#memanggil fungsi
hello_world()
hello_world()

#def2
def nama(nama):
    print("ibu"+nama)

#m2
nama("putri")
nama("dinda")
nama("sofi")

#def3
def say(nama,prodi):
    print("hello nama saya adalah",nama)
    print("program studi saya adalah", prodi)

#m3
say ("fatiya","TI")    

#def4
def jumlah(a,b):
    jumlah=a+b
    print(jumlah)

#def5 kalau tidak dilist
def say(nama,prodi):
    print("hello nama saya adalah",nama)
    print("program studi saya adalah", prodi)

#m5
say ("fatiya","TI") 

#def6
def perkalian(x):
    print(perkalian(4))

#m6
    return x*2

#def7 luas persegi
def hitungluas(sisi):
    luas=(sisi*sisi)
    print("luas persegi adalah", hitungluas(5))

#m7
    return luas

#def8 pangkat
def pangkat(a,b):
    print(pangkat("2","2"))
    
#m8
    return a**b