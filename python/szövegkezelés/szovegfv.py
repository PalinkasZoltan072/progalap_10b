def nagybetusse(s):
    sz = ''
    for i in range(len(s)):
        if s[i] >= "a":
            sz += chr(ord(s[i])-32)
        else:
            sz += s[i]
    return sz



a = '"'
b = "'"
print(b + a + b)

print("\'\"\'")

print(chr(39) + chr(34)+ chr(39))

print(chr(ord("'")) + chr(ord('"')) + chr(ord("'")))

v = "Budapest"
nagybetus = v.upper()
kisbetus = v.lower()
cserelt = v.swapcase()

print(nagybetus, kisbetus, cserelt)

nev = "nemecsek erno"

tnev = nev.title()
print(nev, tnev)

mondat = "a mondatokat nagy kezdobetuvel kezdjuk"
nagymondat = mondat.capitalize()
print(mondat)
print(nagymondat)



sajat_nagybetus = nagybetusse(v)
print(sajat_nagybetus)





#Logikai fuggvenyek
szoveg = "5123"
if szoveg.isdigit():
    print("szam")
elif szoveg.isalpha():
    print("csak betuk")
elif szoveg.isalnum():
    print("szamok es betuk")
else :
    print("nem szam")


sz = "Budapest"
if sz.isupper():
    print("csupa nagybetu")
elif sz.islower():
    print("csupa kisbetu")
else:
    print("Van nagy es kis betu is")

if sz.startswith("Buda"):
    print("Ezzel kezdodik: Buda")
if sz.endswith("pest"):
    print("Ezzel vegzodik: vegzodik")


#Eltavolitasok
noveny = "almafa"
print("kidobott {a, f}:", noveny.strip("af")) # rstrip lstrip

#kereses
print("Elso \"a\ helye:", noveny.find("a"))

#csere
print("alma ->korte:", noveny.replace("alma", "korte"))
