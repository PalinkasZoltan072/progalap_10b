ora = 8
perc = 0

for i in range(0, 12+1): 
    if ora <= 9:
        print("0"+str(ora),str(perc)+"0", sep=":")
    else:
        print(ora,str(perc)+"0", sep=":")
    perc += 5 
    if perc / 6 >= 1:
        perc = perc - 6
        ora = ora +1


