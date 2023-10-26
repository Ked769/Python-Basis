a,b = [float(i) for i in input("Enter the numbers seperated by space : ").split()]
if a>b:
    print(f"{a} > {b}")
else:
    print(f"{b} > {a}")