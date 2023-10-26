c = 0
for i in [int(i) for i in input("Enter elements seperated by space : ").split()]:
    if len(str(i))==2:c+=i
print(f"Sum : {c}")