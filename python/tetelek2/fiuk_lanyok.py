



def fiuk_lanyok_szetvalogat(nemek:list, fiuk:list, lanyok:list):
    for i in range(len(nemek)):
        if  nemek[i] == "f":
            fiuk.append(i)
        else:
            lanyok.append(i)


# a listra listabol kiirja a sorszamok litsa elemeinek
#megfelelo indexu elemeket
def kiiras(lista:list, sorszamok:list):
    for i in range(len(sorszamok)):
        print(lista[sorszamok[i]], end=" ")
    print()


nevek = ["bela", "feri", "sanyi", "erzsebet",
"julia", "soma", "hermione"]
nemek = [ "f", "f", "f", "n", "n", "f", "n",]


fiuk = []
lanyok = []
fiuk_lanyok_szetvalogat(nemek, fiuk, lanyok)
kiiras(nevek, fiuk)
print
kiiras(nevek, lanyok)