for n in [(int(i),int(i)%3) for i in input("Enter elements seperated by space : ").split()]:
    if not n[1]:print(n[0])