#soal pertama
class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print(f"Gempa di {self.lokasi}: Dampak gempa tidak berasa")
        elif 2 <= self.skala < 4:
            print(f"Gempa di {self.lokasi}: Dampak gempa, bangunan retak-retak")
        elif 4 <= self.skala < 6:
            print(f"Gempa di {self.lokasi}: Dampak gempa, bangunan roboh")
        elif self.skala >= 6:
            print(f"Gempa di {self.lokasi}: Dampak gempa, bangunan roboh dan berpotensi tsunami")
