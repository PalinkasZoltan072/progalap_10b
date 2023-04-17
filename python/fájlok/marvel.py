def knev(s):
    eredmeny= ""
    for i in range(len(s)-1):
        eredmeny += s[1]
    return eredmeny




fr = open("marvel.csv", "r")
emberek = fr.readlines()
vnevek = []
knevek = []

for i in range(len(emberek)):
    sor = emberek[i].strip().split(";")
    vnevek.append(sor[0])
    #knevek.append(sor[1].split()[0])
    #knevek.append(sor[1].replace("\n", ""))
    #knevek.append(sor[1][0:1])
    #knevek.append(knev(sor[1]))
    knevek.append(sor[1])


print(vnevek)
print(knevek)
fr.close()