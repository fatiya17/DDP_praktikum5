#perbandingan nilai 2 variabel
a=20
b=15
print(a>b)

#if, elif, else konversi suhu
farenheit= float(input("masukan nilai farenheit :"))
celcius= farenheit-32*5/9
celcius= 5/9*farenheit-32

print("nilai dalam celcius :", celcius, "c")

if farenheit >30:
 print("lebih dari 30")
elif farenheit <30:
 print("kurang dari 30")
else:
 print("farenheit sama dengan celcius")

#status mahasiswa aktif
nama="Fatiya Labibah"
nim="0110223060"
rombel="TI02"
print(nama,nim,rombel)
kehadiran= input("jika hadir =, jika tidak -(=,-) :")
kehadiran1= float (input("masukan angka kehadiran 1"))
kehadiran2= float (input("masukan angka kehadiran kedua"))

if kehadiran == "=":
   hasil= kehadiran1=kehadiran2
   print("aktif")
elif kehadiran == "-":
   kehadiran1-kehadiran2
   print("alfa")

#kalkulator sederhana
print("Kalkulator Sederhana")
angka1= float (input("masukan angka 1 :"))
operator= input("operator (+,-,x,/) :")
angka2= float (input("masukan angka 2 :"))

if operator == "+":
   hasil= angka1+angka2
   print(f"hasilnya adalah {hasil}")
elif operator == "-":
   hasil= angka1-angka2
   print(f"hasilnya adalah {hasil}")
elif operator =="x":
   hasil= angka1*angka2
   print(f"hasilnya adalah {hasil}")
elif operator =="/":
   hasil= angka1/angka2
   print(f"hasilnya adalah {hasil}")

