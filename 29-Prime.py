n,t = int(input("Enter Number : ")),True
for i in range(2,n//2):
    if n%i==0:
        print(f"{n} is Non - Prime")
        t=False
        break
if t:print(f"{n} is Prime")