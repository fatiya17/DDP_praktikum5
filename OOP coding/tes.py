#25
x= 0
y = 10
if 0 == x:
    if y == 10:
        print("Yes")

z = 41

#28
if z > 10:
    print("Dibawah 10")
    if z > 20:
        print("Dan juga dibawah 20")
    else:
        print("Tapi tidak dibawah 20")

#33
    for i in [2,1,5,"apel","jeruk"]:
        print(i)

#13
for n in "banana":
    print(n)

#23
words = "His e-mail is in-fo@nurulfikri.ac.id"
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]

#29
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()

#2
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1

#12
class PartyAnimal:
    x = 0
    name =  ''
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructured')
    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

q =  PartyAnimal('Quincy')
m = PartyAnimal('Miya')
q.party() 
m.party()
q.party()

#26
#width = 15
#height = 12.0
#print(height/3)

#32
#def fred():
#    print("Zap")
#def jane():
#    print("ABC")

#jane()
#fred()
#jane()

#36
#fruit = "banana"
#x = fruit[1]
#print(x)

#37
#counts = {'chuck': 1, 'annie': 42, 'jan': 100}
#for key in counts:
 #   if counts[key]>10:
   #  print(key, counts[key])

#9
for i in [2,1,5,"apel","jeruk"]:
        print(i) 

#2
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1
#40
# a = 33
# b = 200
# if b > a:
# print(a)
# else:
# print(b)
# else:
# print("kode salah")


