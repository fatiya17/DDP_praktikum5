class Orang:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def makan (self):
        print("saya bisa makan")

    def cetak(self):
        print("Nama saya", self.fname, self.lname)

class Mahasiswa (Orang):
    def __init__(self, fname, lname, prodi, angkatan):
        super().__init__(fname, lname)
        self.prodi = prodi
        self.angkatan = angkatan

    def print(self):
        print("Saya Prodi", self.prodi, self.angkatan)

class Pegawai(Orang):
    def bekerja(self):
        print("Saya Bekerja")

#objek orang
x = Orang("Bagas","Maulana")
x.cetak()
#x.bekerja()

#objek mahasiswa
y = Mahasiswa("Sulastri", "Astuti", "Teknik Informatika", 2023)
y.print()
y.cetak()
y.makan()

#objek pegawai
agus = Pegawai("Anton", "Agus")