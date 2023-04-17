osztalyzat = int(input("Osztalyzat: "))

if osztalyzat  < 1 or osztalyzat > 20:
    print("hibas")
    exit()

if osztalyzat <= 10:
    print("Bukott 1<=osztalyzat<=20 kellene")
else:
    print ("atment")
  
print("Program vege!")