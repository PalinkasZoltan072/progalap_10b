#beolvasas
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
#feldolgozas
maximum = a
if b > maximum:
    maximum=b
if c > maximum:
    maximum=c

#kiiras
print("max:", maximum)