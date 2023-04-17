
a2 = input("osztály: ")
a = int(input("pontszám: "))
d = 60
if a2 == a:
    d = d - a
    print("Nyertek a közgazdászok!", "Csak", d, "pontot vesztettek!")
elif a2 == b:
    d = d - a
    print("Győztek a gazdinfósok!", "Csak", d, "pontot vesztettek!")
else:
    d = d - a
    print("Infósok a legjobbak!", "Csak", d, "pontot vesztettek!")