class animal :
    jumlah_kaki = 0
    memiliki_paruparu =""
    jenis_kulit =""
    jenis =""
    BKSDA = 'berikut ini adalah katagori hewan dilindungi'

def __init__(self,jumlah_kaki,memiliki_paruparu,jenis_kulit,jenis):
    self.jumlah_kaki = jumlah_kaki
    self.memiliki_paruparu = memiliki_paruparu
    self.jenis_kulit = jenis_kulit
    self.jenis = jenis

def jenis(self,golongan):
    #self kategori =self.kategori + jenis
    self.jenis += golongan

def cetak(self):
    print(animal.BKSDA,
           '/n hewan berkaki dua :',format(self.jumlah_kaki,','),
              '/n alat pernafasan :',self.memiliki_paruparu,
              '/n bagai mana jenis kulitnya :',self.jenis_kulit
            )



