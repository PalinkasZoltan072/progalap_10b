def a_minus_b_kepzes(a, b):
    d = []
    for i in range(len(a)):
        if a[i] not in b[i]
        d.append()


    return d

def a_minus_b_kepzes(a:list, b:list):
    d=[]
    for i in range(len(b))

def metszet_kepzes(a:list, b:list):
    m = []
    for i in range(len(a)):
        if a[i] in b:
            m.append(a[i])
    return m # m.copy

def unio_kepzes(a:list, b:list):
    u = []
    for i in range(len(a)):
        u.append(a[i])
    for i in range(len(b)):
        if b[i] not in u:
            u.append(b[i])
    return u

matekosok = ["Anna", "Béla", "Csaba", "Dóra", "Erik", "Ferenc"]
progosok = ["Ferenc", "József", "Dóra", "Anna", "Csaba"]

metszet=metszet_kepzes(matekosok, progosok)
print(metszet)
metszet2=metszet_kepzes(progosok, matekosok)
print(metszet2)

unio = unio_kepzes(matekosok, progosok)
print(unio)

csak_matekos = a_minus_b_kepzes(matekosok, progosok)
csak_progosok = a_minus_b_kepzes(progosok, matekosok)
