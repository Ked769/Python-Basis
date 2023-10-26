p,r,t=[float(i) for i in input(\
    "Enter principal(rs), rate(%) and time(y) seperated by a space : ").split()]
print("Simple interest is : ", p*r*t*0.01)