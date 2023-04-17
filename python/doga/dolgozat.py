a = float(input("1. pont: "))
b = float(input("2. pont: "))
c = float(input("3. pont: "))
jo = a >= 80 and b >= 80 and c >= 80
atlag=(a+b+c)/3

while not jo:
    print("Tanulni kéne! Újraírjuk!")
    a = float(input("1. pont: "))
    b = float(input("2. pont: "))
    c = float(input("3. pont: "))
print (round(atlag, 2), "%" )
    


