#while
a = 0
while a <= 3:
        print(a)
        a += 1

a=1
while a<=10:
    b=1
    while b<=10:
        print(a*b, end=" ")
        b+=1
        print ()
        a+=1

#for
for i in range(1,8):
    print (i)        

for i in range (50):
    print (i)

for i in range (0,31,3):
    print (i)

for i in range (50,0,-5):
    print (i)   

for i in range (3):
    print ("TI02")

for i in range (1,11):
    print(i)
for j in range (1,11):
    print(j)
k = i*j
print (k, end=' ')
print()

#break statement
i = 1
while i < 6:
     print(i)
     if i == 3:
      i += 1

a=1
while a<6:
    print (a)
    if a==3:
        break
    a+=1

#continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i tidak lebih besar dari  6")
