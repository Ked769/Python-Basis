n = int(input("Enter no. of rows : "))
last = 1
l1 = (n*(n-1)//2) + 1
l2 = (n*(n+1)//2)
n_sp = 0
for num in [str(i) for i in range(l1,l2+1)]:
    n_sp += len(num)
n_sp = n_sp//2
for i in range(1,n+1):
    print(" "*(n_sp-i), end = "")
    for j in range(last,i+last):
        print(j, end = "")
    last += i
    print()