a = dict()
for x in tuple((int(i[0]),i[1]) for i in (n.split(":") for n in (input("Enter vals |rollNo:Name| : ").split()))):
    a[x[0]] = x[1]
print(a)