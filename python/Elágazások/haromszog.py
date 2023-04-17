a = int(input("a "))
b = int(input("b "))
c = int(input("c "))

#feldolgozas
if a + b > c and b + c > a and c + a > b:
    print("igen")
else:
    print("nem")