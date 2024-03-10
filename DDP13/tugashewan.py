class Hewan:
    def __init__(self, nama, makanan, habitat, perkembangbiakan):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.perkembangbiakan = perkembangbiakan

    def info_nama(self):
        print(f"Nama: {self.nama}")

    def info_makan(self):
        print(f"Makanan: {self.makanan}")

    def info_hidup(self):
        print(f"Hidup di: {self.habitat}")

    def info_berkembang_biak(self):
        print(f"Berkembang biak dengan cara: {self.perkembangbiakan}")


class Badak(Hewan):
    def __init__(self, habitat):
        super().__init__("Badak", "tumbuhan", habitat, "vivipar")

    def serang_dengan_cula(self):
        print(f"{self.nama} menyerang dengan menggunakan cula.")


class Ikan(Hewan):
    def __init__(self, habitat):
        super().__init__("Ikan", "plankton", habitat, "ovipar")

    def berenang(self):
        print(f"{self.nama} sedang berenang.")


class Ular(Hewan):
    def __init__(self, habitat):
        super().__init__("Ular", "hewan kecil", habitat, "ovipar")

    def merayap(self):
        print(f"{self.nama} sedang merayap.")


# Contoh penggunaan
badak = Badak("hutan")
badak.info_nama()
badak.info_makan()
badak.info_hidup()
badak.info_berkembang_biak()
badak.serang_dengan_cula()

ikan = Ikan("kolam")
ikan.info_nama()
ikan.info_makan()
ikan.info_hidup()
ikan.info_berkembang_biak()
ikan.berenang()

ular = Ular("hutan")
ular.info_nama()
ular.info_makan()
ular.info_hidup()
ular.info_berkembang_biak()
ular.merayap()
