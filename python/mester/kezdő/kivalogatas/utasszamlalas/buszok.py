
def kivalogatas(buszok:list, m):
    zsufolt=[]
    ures=[]
    for i in range(len(buszok)):
        if buszok[i] / m >= 0.80:
            zsufolt.append(i)
        elif buszok[i] / m <= 0.20:
            ures.append(i)
    return zsufolt, ures





def main():
    sor= input().split()
    n = int(sor[0])
    m = int(sor[1])
    buszok = []
    for i in range(n):
        busz = int(input())
        buszok.append(busz)
    
    kivalogat=kivalogatas(buszok, m)

main()
zsufolt=[   ]

