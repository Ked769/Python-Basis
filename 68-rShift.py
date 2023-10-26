res = []
lst = [int(i) for i in input("Enter elements seperated by space : ").split()]
res.append(lst[-1])
res.extend(lst)
res.pop(-1)
print(res)