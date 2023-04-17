a = int(input("ketto szamjegyu vagy tobb: "))

jo = (a % 10) % 3 == 0
while not jo:
    a = int(input("ketto szamjegyu vagy tobb: "))
    jo = (a % 10) % 3 == 0
