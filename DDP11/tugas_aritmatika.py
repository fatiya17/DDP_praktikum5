#buat aritmatika (min 10)

import math
def tambah(bil1, bil2):
   hasil = bil1+bil2
   print("hasil tambah dari",bil1,"+",bil2,"=",hasil)

def kurang(bil1, bil2):
   hasil = bil1-bil2
   print("hasil pengurangan dari",bil1,"-",bil2,"=",hasil)

def kali(bil1, bil2):
   hasil = bil1 * bil2
   print("hasil perkalian dari",bil1,"*",bil2,"=",hasil)

def bagi(bil1, bil2):
   hasil= bil1 / bil2
   print("hasil pembagian dari",bil1,"/",bil2,"=",hasil)

def pangkat(bil1, bil2):
   hasil = math.pow(bil1, bil2)
   print("hasilpemangkatan dari",bil1,"^",bil2,"=",hasil)
   
def modulus (bil1, bil2 ) :
    hasil = bil1 % bil2
    print ("hasil modulus dari", bil1, "&", bil2, "adalah", hasil)

def akar (bil1, bil2 ) :
    bil2 = 0.5
    hasil = bil1 ** bil2
    print ("hasil akar dari", bil1, "adalah", hasil)

def bulatkan_kebawah (bil1, bil2) :
    hasil = bil1 // bil2
    print ("hasil bulatkan kebawah dari", bil1, "dan", bil2, "adalah",hasil)

def bulatkan_keatas (bil1) :
    hasil = math.ceil(bil1)
    print ("hasil bulatkan keatas dari", bil1, "adalah", hasil)

def dibulatkan (bil1 ) :
    hasil = round (bil1)
    print ("hasil", bil1,"dibulatkan adalah", hasil)