res,l,i = [],[int(i) for i in input("Enter elements seperated by space : ").split()],0
while i in range(0,len(l)):
    if not l[i]%10:
        res.extend([l[i+1],l[i]])
        i += 2
    else:
        res.append(l[i])
        i += 1
print(res)