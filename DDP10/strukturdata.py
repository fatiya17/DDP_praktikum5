#array : menggunakan kurung siku
A = [1,2,3,4]
print (A[2])

#set : tidak bisa diubah, tidak boleh ada yang double, tidak berurutan outputnya
'''add : buat nambah, remove : hapus'''
B = [1,2,3,4]
print (B)

set1 = {1,2,3}
set2 = {2,4,6}
set3 = set1.union(set2)
print(set3)

set1 = {1,2,3}
set2 = {2,4,6}
set1.update(set2)
print(set1)

#stack : LIFO, masuk pertama= keluar terakhir

C = [1,2,3,4]
D = C.pop ()
C.append(6)
print (C)
print (D)

#queque : FIFO, masuk pertama keluar pertama (antri)
E = [1,2,3]
E.append (6)
F = E.pop (0)
print (E)
print (F)

#Dictionary : Dituliskan dengan diapit kurung kurawal { } dan dipisah dengan titik dua
data_diri = {"nama":"Reza",
"matpel":"DDP"}
data_diri["semester"] = 1
print(data_diri["nama"])

'''Mengakses dengan key, cth:'''
x = data_diri['nama'] # bisa juga data_diri.get('nama')
'''Mengubah value'''
data_diri['nama']="Dian"
'''Menambah entri'''
data_diri['alamat'] = "Jakarta"
'''Menghapus key'''
data_diri.pop('alamat')
'''Mengecek keberadaan key, pakai operator in'''
if('nama' in data_diri):
    print('nama ada di data_diri')
