x= [7, 9, 12, 3, -5, -2, 8, -5, 18, -1]
n = len(x)
a = 1
b = 0
#parosak szama?
for i in range(n):
    if x[i] % 2 == 0:
        b += 1
print(b)

    
#legnagyobb ertek
c = x[0]
for i in range(1, n):
    if c < x[i]:
        c = x[i]
print(c)
# paros szamok szorzata
for i in range( n):
    if 0 > x[i]:
        a *= x[i]
print(a)

'''
maxi
for i in range(1, n):
    if x[i] > x[maxi]:
        maxi = i

'''
#legkisebb elem index
d = 0
for i in range(1, n):
    if x[i] <= x[d]:
        d= i
print(d)

#atlag
atlag=0
f = 0
for i in range(n):
    f =+ x[i]
 atlag = f/n
print(atlag)
