#be: (egesz)
#ki primszam-e (primszam / nem primszam)
n=int(input("n: "))


prime= True 
i = 2
while i < n // 2 and prime:
    if n % i == 0:
        prime = False
        print(i)
    i += 1 

if prime:
    print("primszam")
else:
    print("nem prim")