def minidex(x:list, i:list):
    mini = i
    for j in range(i+1, len(x)):
        if x[j] < x[mini]:
            mini = j
    return mini




#haladjunk vegig a tombon es az aktualis elemet csereljuk meg a hatralevominimummal
def rendezes_minimum(x):
    for i in range(len(x)-1):
        mini=minidex(x, i)#i-edik legkisebb indexet
        seged = x[i]
        x[i] = x[mini]
        x[mini]=seged
        #x[i], x[mini] = x[mini] , x[i] csere






def main():
    x = [3, 5, 2, 1, 3]
    print(x)
    rendezes_minimum(x)
    print(x)

#main()