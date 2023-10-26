n=c=0
for i in tuple(float(i) for i in input("Enter elements seperated by space : ").split()):
    n,c = n+i,c+1
print(f"Sum : {n}\nAverage : {n/c}")