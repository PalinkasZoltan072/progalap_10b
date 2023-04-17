fr = open("emberek.csv", "r")
emberek = fr.readlines()
nevek = []
korok = []

for i in range(len(emberek)):
    sor = emberek[i].split(";")
    nevek.append(sor[0])
    korok.append(int(sor[1]))


print(nevek)
print(korok)
fr.close()