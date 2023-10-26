marks = [float(i) for i in input("Enter the marks for the subjects(seperate with space) : ").split()]
n=0
for i in marks:
    n += i
print("Average marks is : ", n/len(marks))