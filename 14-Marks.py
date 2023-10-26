def div(n):
    if n >= 60:
        print("1st Division")
    elif n < 60 and n >= 50:
        print("2nd Divison")
    elif n < 50 and n >= 40:
        print("3rd Division")
    else:
        print("Failed")

marks,n = [float(i) for i in input("Enter marks seperated by space : ").split()],0
for i in marks:
    n += i%100.00001
    print(f"Subject {marks.index(i)+1} percentage :\t{format(i%100.00001,'.2f')}%\t",end="")
    marks[marks.index(i)] = ""
    div(i%100.00001)
print(f"Total : {n//1} marks\t{format(n/5,'.2f')}%", end = "\t")
div(n//5)