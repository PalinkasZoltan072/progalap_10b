n = int(input())
idok = []
for i in range(n):
    idok.append(int(input()))

i = 1
while i < n and not(idok[i] < idok[i-1]):
    i += 1
if i < n:
    sorszam=i+1
else:
    sorszam=i-1
