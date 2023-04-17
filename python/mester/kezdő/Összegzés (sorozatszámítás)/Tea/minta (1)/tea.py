n =(int(input))

tea =[]
db =[]
for i in range(n):
    #fajta beolvas
    tea = input()
    tea.append(tea)
    #menny beolvasas
    db=int(input())
    db.append(db)
#print(tea, db)
#feldolgozas
s = 0   
elsofajta=tea[0]
for i in range(n):
    if tea[i] == elsofajta:
        s += db
print(s)
 
'''
s = mennyisegek[0]
for i in range(1, n):
    if fajtak[i] == fajtak[0]:
        s += mennyisegek[i]
'''