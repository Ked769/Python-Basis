res = lst = [int(i) for i in input("Enter elements seperated by space : ").split()]
res.append(res[0])
res.pop(0)
print(res)