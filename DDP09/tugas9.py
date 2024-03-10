#no 1 buatlah fungsi untuk menampilakan data diri :
'''contoh pemanggilan : profil(nama, alamat, gender, umur, hoby)'''

print("Data Diri :")
def datadiri(nama,alamat,gender,umur,hobi):
    print("Nama",nama)
    print("Alamat",alamat)
    print("Gender",gender)
    print("Umur",umur)
    print("Hobi",hobi)

datadiri("fatiya","klapanunggal","perempuan","17","tidur")   

#no2 buatlah fungsi untuk mencari kelulusan nilai dari berikut : 
'''jika nilai < 60 maka gagal 
jika nilai = 61 - 70 maka baik 
jika nilai = 71 - 80 maka sangat baik 
jika nilai = 81 - 100 maka istimewa

ex:
nilai (60)'''

print("Predikat :")
def kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif nilai == 60:
        return "Gagal"
    elif nilai >= 61 and nilai <= 70:
        return "Baik"
    elif nilai >= 71 and nilai <= 80:
        return "Sangat Baik"
    elif nilai >= 81 and nilai <= 100:
        return "Istimewa"

print(kelulusan(71))

#no 3 buatlah fungsi untuk mencetak nilai bilangan ganjil dari parameter yang di masukan :
'''ex : ganjil (100)'''

print("Bilangan Ganjil :")
def bilangan_ganjil(batas):
    for i in range(batas+1):
        if i % 2 != 0:
            print(i)


bilangan_ganjil(30)