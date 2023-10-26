def style1(n):
    for i in range(n+1):
        print("*"*i)
def style2(n):
    for i in range(n+1):
        print(f"{i}"*i)
def style3(n):
    for row in range(n+2):
        for j in range(1,row):
            print(j,end = "")
        print()
def style4(n):
    last = 1
    for row in range(n+1):
        for i in range(row):
            if last>9:
                print(last,end=" ")
            else:
                print(last,end="  ")
            last += 1
        print()

def style5(n):
    for i in range(2,2*(n+1),2):
        print(f"{i} "*(i//2))
n = int(input("Enter no. of rows : "))
x=int(input("Enter style number(1-5): "))
if x == 1:
    style1(n)
elif x == 2:
    style2(n)
elif x == 3:
    style3(n)
elif x == 4:
    style4(n)
else:
    style5(n)