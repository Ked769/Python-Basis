lst,res = [int(i) for i in input("Enter elements seperated by space : ").split()],[]
if int(input("Enter 1 to calculate without reverse() or 0 for with : ")):
    for i in range(len(lst)-1,-1,-1):
        res.append(lst[i])
else:
    lst.reverse()
    res = lst
print(res)
