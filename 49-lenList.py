l = input("Enter elements seperated by space : ").split()
if int(input("Enter 1 to do with len() or 0 without : ")):
    print(f"Length of list {l} : {len(l)}")
else:
    c = 0
    for i in l:c+=1
    print(f"Length of list {l} : {c}")