f = [0,1]
for i in range(int(input("Enter n : "))+1):
    print(f"Term {i} : {f[-2]}")
    f.append(f[-1]+f[-2])