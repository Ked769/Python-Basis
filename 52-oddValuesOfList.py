for n in [(int(i),int(i)%2) for i in input("Enter elements seperated by space : ").split()]:
    if n[1]:print(n[0])