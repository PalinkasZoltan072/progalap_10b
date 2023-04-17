n = int(input("n: "))
szam = 1



for i in range(1, n+1):
    for j in range(i):
        print(szam, end=" ")
        szam += 1
    print()
    
    