ev = int(input("2000 utani ev: "))

if ev>=2000:
    if ev%4 == 0:
        print("szokoev")
    else: 
        print("nem szokoev")
else:
    print("buta vagy bocs! 2000 utanni ev kellene")