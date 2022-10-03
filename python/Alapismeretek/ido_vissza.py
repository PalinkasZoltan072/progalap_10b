ido = int (input("Masodperc: ")) #3723

#feldolgozás
ora = ido // 3600
maradek = ido % 3600 #123
perc = maradek // 60 #2
masodperc =maradek % 60 #3


#Kiiras
print("eltelt ido:", ora, "ora", perc, "perc", masodperc, "masodperc")