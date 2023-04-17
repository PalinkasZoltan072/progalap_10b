x = float(input("x"))

 
bal = 0
jobb = x
# print(bal, jobb)

for i in range(50):
    felezo= (bal+jobb) / 2
    if felezo*felezo < x: #jpbb intervallumban megy tovabb
        bal = felezo
    else:
        #balban megyunnk tovabb
        jobb = felezo
    # print(bal, jobb)
print(x, "negyzetgyok:", round(felezo, 4))