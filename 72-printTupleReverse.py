lst = tuple(int(i) for i in input("Enter elements seperated by space : ").split())
for i in range(len(lst)-1,-1,-1):
    print(lst[i])