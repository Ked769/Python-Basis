d = dict()
for i in range(3,100,3):
    d[i]=i**2
try:print("Value :",d[(int(input("Enter key value : ")))])
except KeyError:print("Not Found")