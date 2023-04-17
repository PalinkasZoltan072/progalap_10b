n = int(input("osztalyzat: "))
jo = 1 <= n and n <= 5
while not jo:
    n = int(input("osztalyzat: 1<osztalyzat<=5  "))
    jo = 1 <= n and n <= 5