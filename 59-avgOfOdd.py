c,n = 0,0
for i in [int(i) for i in input("Enter elements seperated by space : ").split()]:
    if i%2!=0:c,n=c+i,n+1
print(f"Average of odds : {c/n}")