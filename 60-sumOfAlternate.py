s,T = 0,True
for i in [int(i) for i in input("Enter elements seperated by space : ").split()]:
    if T: s += i
    T = not T
print("Sum :",s)