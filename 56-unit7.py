for i in [(int(i),(int(i)-7)%10) for i in input("Enter elements seperated by space : ").split()]:
    if not i[1]:print(i[0])