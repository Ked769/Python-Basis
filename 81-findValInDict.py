d = dict()
for i in range(3,100,3):
    d[i]=i**2
x = int(input("Enter value : "))
try : print("Value :",[k for (k, v) in d.items() if v == x][0])
except IndexError:print("Not Found")