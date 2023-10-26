m = [i for i in input("Enter operation in full(seperate with space): ").split()]
a,b,o = float(m[0]),float(m[2]),m[1]
if o=="+":
    print("Result : ", a+b)
elif o=="-":
    print("Result : ", a-b)
elif o=="*":
    print("Result : ", a*b)
elif o=="/":
    print("Result : ", a/b)
elif o=="//":
    print("Result : ", a//b)
else:
    print("Result : ", a**b)