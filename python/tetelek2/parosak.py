#Valogassuk ki a paros szamokat!

x = [ 7, 3, 4, 2, 1, 0, -8]
y =[]
for i in range (len(x)):
    if x[i] % 2 == 0:
        y.append(x[i])

print(y)