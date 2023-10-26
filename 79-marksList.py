a=dict()
for i in range(int(input("Enter no. of students : "))):
    a[input("Enter name : ")] = tuple(int(i) for i in input("\nEnter marks seperated by space : ").split())
print("\n",a)