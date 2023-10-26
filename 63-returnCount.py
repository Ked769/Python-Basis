def woC(lst,n):
    c = 0
    for i in lst:
        if i == n: c += 1
    return c
def wC(lst,n):
    return lst.count(n)
lst,n = [i for i in input("Enter elements seperated by spaces : ").split()], input("Enter term to be counted : ")
print(f"Count : {[woC(lst,n), wC(lst,n)][int(input('0 for without count, 1 for with count : '))]}")