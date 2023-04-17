

#Valogassuk ki a paros szamokat!

x = [ 7, 3, 4, 2, 1, 0, -8]
y =[]
for i in range (len(x)):
    if x[i] % 2 == 0:
        y.append(i)

#print(x)
#print(y)
for i in range(len(y)):
    print(y[i], end=" ")
print()
for i in range(len(y)):
    print(x[y[i]], end=" ")