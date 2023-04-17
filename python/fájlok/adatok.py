fr = open("adatok.txt", "r")
szamok = fr.read().split()
for i in range (len(szamok)):
    szamok[i] = int(szamok[i])
print(szamok)
fr.close()