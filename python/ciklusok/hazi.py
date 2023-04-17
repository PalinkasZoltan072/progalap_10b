# n = int(input("n: "))

# osszeg = 0

# for i in range(1, n+1, 2):
#     osszeg +=1
#     print(i)


# print (osszeg)




# beolvasas
a = int(input("a: "))
b = int(input("b: "))
csere = 0
c=1


# feldolgozas
while a == b:
    print("nem lehet egyenlő")
    a = int(input("a: "))
    b = int(input("b: "))

if a > b:
     csere = a
     a = b
     b = csere
    

if a %2 == 0:
    for i in range(a+1, b+1, 2):
        c *= i
    print("=", c)

else:
    for i in range(a, b+1, 2):
        c *= i
    print("=", c)
 