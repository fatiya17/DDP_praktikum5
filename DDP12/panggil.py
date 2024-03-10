# info_gempa.py
from gempa import*

# Membuat objek gempa
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)

# Memanggil fungsi dampak() pada masing-masing objek gempa
print(f"Gempa 1 ({gempa1.lokasi}): {gempa1.dampak()}")
print(f"Gempa 2 ({gempa2.lokasi}): {gempa2.dampak()}")
print(f"Gempa 3 ({gempa3.lokasi}): {gempa3.dampak()}")
print(f"Gempa 4 ({gempa4.lokasi}): {gempa4.dampak()}")
print(f"Gempa 5 ({gempa5.lokasi}): {gempa5.dampak()}")
