#be: (egesz)
#ki 1-tol n-ig orim szam
#pl m = 23 -> 2 3 5 7 11 13 17 19 23

m = int(input("m: "))
print(2, end="")
j= 3
while j <= m:
    
    n = j
    prime=True

    i = 2

    while i < n // 2 and prime:
        if n % i == 0:
            prime = False
        i += 1 
    if prime:
        print(j, end=" ")






