c = 0
for i in [(int(i),int(i)%3) for i in input("Enter elements seperated by space : ").split()]:
    if not i[1]:c+=i[0]
print(f"Sum : {c}")