# Gempa.py

class Gempa:
    def _init_(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("Dampak gempa tidak berasa di", self.lokasi)
        elif 2 <= self.skala < 4:
            print("Dampak gempa: Bangunan retak-retak di", self.lokasi)
        elif 4 <= self.skala < 6:
            print("Dampak gempa: Bangunan roboh di", self.lokasi)
        elif self.skala >= 6:
            print("Dampak gempa: Bangunan roboh dan berpotensi tsunami di", self.lokasi)
