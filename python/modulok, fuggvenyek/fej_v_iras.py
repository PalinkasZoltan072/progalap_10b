from random import *

be = input("Fej v Iras")
if be != "F" and be != "I":
    exit

#F == 1, I == 2
vel = randint(1, 2)

if vel == 1:
    erme = "F"
else:
    erme = "I"
print("Dobas:", erme)

#gyozott?
if be ==erme:
    print("nyertel")
else:
    print("nyertel           ")