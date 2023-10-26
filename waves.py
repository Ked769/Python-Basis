n = int(input("Enter no. of repetitions : "))
for i in range(1,n+1):
    print(0)
    for j in range(1,i+1):
        for k in range(1,j+1):
            print(k, end="")
        print()
    for j in range(i-1,0,-1):
        for k in range(1,j+1):
            print(k, end="")
        print()