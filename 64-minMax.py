def wMinMax(lst):
    return min(lst), max(lst)
def woMinMax(lst):
    return sorted(lst)[-1], sorted(lst)[0]
lst = [int(i) for i in input("Enter elements seperated by space : ").split()]
if int(input("Enter 0 for calculation without min max function, or 1 for with : ")):
    res = wMinMax(lst)
    print(f"Minimum : {res[0]}\nMaximum : {res[1]}")
else:
    res = woMinMax(lst)
    print(f"Minimum : {res[0]}\nMaximum : {res[1]}")