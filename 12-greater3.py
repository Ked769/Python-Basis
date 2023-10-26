a = [float(i) for i in input("Enter the numbers seperated by space : ").split()]
a.sort(reverse=True)
print(f"{a[0]} > {a[1]} > {a[2]}")