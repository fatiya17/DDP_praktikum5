# acces modifier = dapat diubah dari luar karena bersifat publik
# privat acces = __gaji (underscore 2x)
# method dapat membaca yang prvat dengan self
class Player:
    #atribut
    name = "fatiya"
    __salary = 1_000_000

    #method
    def get_salary(self):
        return self.__salary

#panggil
player = Player()
player.name = "fatiya labibah"
player.salary = 3_000_000

print(f"{player.name} berhasil dibuat")
print(player.get_salary())
print(player.salary)
