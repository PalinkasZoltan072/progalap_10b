from random import randint

def feltolt(n):
    x = []
    for i in range(n):
        r = randint(150, 190)
        x.append(r)
    return x


def rendez_kozepso(magassagok, nevek):
    n= len(magassagok)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if magassagok[j] > magassagok[j+1]:
                magassagok[j], magassagok[j+1] = magassagok[j+1], magassagok[j]
                nevek[j], nevek[j+1] = nevek[j+1], nevek[j]

    

def kiir(m, n):
    for i in range(len(m)):
        print(n[i], ": ", m[i], sep = "")

def main():
    nevek = ["Adam", "Bela", "Csaba", "Denes", "Erik", "Feri", "Gergo", "Hedvig", "Imre", "Jani", "Karoly"]
    magassagok = feltolt(11)

    print("Rendezes elott:")
    kiir(magassagok, nevek)

    print("\nRendezes utan:")
    rendez_kozepso(magassagok, nevek)
    kiir(magassagok, nevek)

    k = len(magassagok) // 2
    print("\nKozepen:", nevek[k])

main()