class Player:
    def __init__(self, health=100, energy=100):
        self.healt = health
        self.energy = energy
       
    def attack(self, target, damage=1):
        target.health -= damage
        self.energy -= damage #self.y - damage
        print(f"attack to monster, monster health: {target.health} & your energy is {self.energy} left")

class Monster:
    def __init__(self, health=100):
        self.health = health #dinamis
        self.health_init = self.health #tetap 500
    
    def attack(self):
        if self.health < self.health_init:
            print("dragon serang balik!")
        else:
            print("dragon zzZZ")

# panggil dan simpan nilai
player1 = Player()
player2 = Player()
dragon = Monster(health=500)

#player.attack()
player1.attack(target=dragon, damage=80) #penyerangan1
player2.attack(target=dragon, damage=20) #penyerangan2

dragon.attack()

#print(monster.__dict__)
#print(player.__dict__)