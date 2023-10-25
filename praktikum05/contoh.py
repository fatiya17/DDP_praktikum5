#element list
a= [1,2,3,4,5]
nama= ["fatiya","sofi","alya"]
profil=["01234","fatiya",19,40.5,160]

print(nama[2])
print(profil[3])

#menambahhkan dan menghapus element list
nama2= ["fatiya","sofi","alya"]
nama2.append("layla")
profil2=["01234","fatiya",19,40.5,160]
profil2.insert(2,"perempuan")

nama2.remove("sofi")

print(nama2)
print(profil2)

#match

ket= '''Selamat datang di aplikasi cuaca masukan pilihan:
1. untuk cuaca panas
2. untuk cuaca hujan
3. untuk cuaca badai'''

print(ket)

cuaca=input ("apakah cuaca hari ini?")

match cuaca:
    case "1":
        print("ke kampus pakai mobil")
    case "2":
        print("ke kampus pkai jas hujan")
    case "3":
        print("tidak berangkat ke kampus")