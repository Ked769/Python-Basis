res = []
for i in [int(i) for i in input("Enter elements seperated by space : ").split()]:
    res.append([10,5][i%2]+i)
print(res)