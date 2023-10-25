#tambahkan 2 list diakhir
variabel= ["motor","matic","125","putih","2"]
variabel.append ("20.000.000")
variabel.append ("sport")

#tambahkan merk kendaraan setelah jenis kendaraan
variabel.insert (2,"vario")
print  (variabel)

#match luas bangun datar

ket=''' Selamat datang di aplikasi menghitung luas bangun datar
masukan pilihan:
1. untuk menghitung luas persegi
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga
'''
print(ket)
luasbd=input ("menghitung luas apa?")

match luasbd:
    case "1":
        print("kamu memilih 1 untuk menghitung luas persegi")
        sisi= int (input("masukan sisi:"))
        luasP= sisi*sisi
        print("luas persegi yang sisinya", sisi, "adalah", luasP)
    case "2":
        print("kamu memilih 2 untuk menghitung luas lingkaran")
        jari2= float (input("masukan jari2:"))
        luasL= 3.14*jari2*jari2
        print("luas lingkaran", jari2, "adalah", luasL)
    case "3":
        print("kamu memilih 3 untuk menghitung luas segitiga")
        alas= int (input("masukan alas:"))
        tinggi= int (input("masukan tinggi"))
        luasS= 1/2*alas*tinggi
        print("luas segitiga", alas, tinggi, "adalah", luasS)
    case _:
        print("salah memilih angka")
