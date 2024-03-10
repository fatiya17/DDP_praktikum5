# info_gempa.py
from gempa2 import*

# Membuat objek gempa
gempa_banten = Gempa("Banten", 1.2)
gempa_palu = Gempa("Palu", 6.1)
gempa_cianjur = Gempa("Cianjur", 5.6)
gempa_jayapura = Gempa("Jayapura", 3.3)
gempa_garut = Gempa("Garut", 4.0)

# Memanggil fungsi dampak untuk masing-masing objek gempa
print("\nDampak Gempa Banten:")
gempa_banten.dampak()

print("\nDampak Gempa Palu:")
gempa_palu.dampak()

print("\nDampak Gempa Cianjur:")
gempa_cianjur.dampak()

print("\nDampak Gempa Jayapura:")
gempa_jayapura.dampak()

print("\nDampak Gempa Garut:")
gempa_garut.dampak()
