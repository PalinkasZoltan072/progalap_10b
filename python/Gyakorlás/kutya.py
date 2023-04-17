év = float(input("kuta éve: "))

if év >= 0 and év <=2:
    c = év*10.5
    print(round(c, 2))
elif év >= 3 :
    d = év*4+21
    print(round(d, 2))
