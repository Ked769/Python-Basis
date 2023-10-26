res = []
for i in [int(i) for i in input("Enter elements seperated by space : ").split()]:
    res.append(int(i%3==0))
print("Result : ", res)