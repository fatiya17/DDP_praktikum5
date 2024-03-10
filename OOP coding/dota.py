class Hero:

#clas variable
    jumlah = 0

    def __init__(self, inputName, inputPower, inputArmor, inputHealth):
        #instance variable
        self.name = inputName
        self.power = inputPower
        self.armor = inputArmor
        self.health = inputHealth
        Hero.jumlah += 1
        print("membuat Hero dengan nama " + inputName)
    
    #method tanpa return
    def siapa(self):
        print("namaku adalah " + self.name)

    #method dengan argumen tanpa return
    def healthUp(self, up):
        self.health += up

    #method dengan return
    def getHealth(self):
        return self.health

print(Hero.jumlah)
hero1 = Hero("sniper", 100, 10, 50)
print(Hero.jumlah)
hero2 = Hero("mirana", 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("ucup", 1000, 100, 0)

print(hero1.name)
print(hero3.armor)
print(hero3.__dict__)

hero1.siapa()
hero1.healthUp(10)

print(hero1.health)
print(hero1.getHealth())
