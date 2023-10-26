n,a = input("Enter number : "),0
for i in n:
    a += int(i)**len(n)
if int(n) == a:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")