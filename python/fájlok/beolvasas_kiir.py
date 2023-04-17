from random import randint


'''
n = int(input())

szamok=[]
for i in range(n):
    szamok.append(float(input()))
print(szamok)
'''
#irasra megnyitok egy fajlt (torli a benne levo tartalmat)
fr = open("be.txt", "r")
n = int(fr.readline())
szamok = []
for i in range(n):
    szamok.append(float(fr.readline()))
fr.close()

fw = open("kimenet.txt", "w")
for i in range(len(szamok)):
    fw.write(str(szamok[i]) + "\n")
fw.write(str(str(randint(1, 20))))
fw.close()


#hozza fuzni a meglevo falj vegehez
fa = open("kimenet.txt", "a")
for i in range(len(szamok)):
    fa.write(str(szamok[i]) + "\n")
fa.write(str(str(randint(1, 20)) + "\n\n"))
fa.close()


#olvas + hozzafuzni
f = open("adatok.txt", "r+") #"r" = read
a = int(f.readline())
b = int(f.readline())
c = int(f.readline())
f.write(str(a) + " " + str(b) + " " + str(c) + "\n")
f.close()


