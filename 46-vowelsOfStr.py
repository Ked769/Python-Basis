n,l = input("Enter string : "), ['a','e','i','o','u']
for i in n:
    if i.lower() in l or i==" ": l.append(i)
print(''.join(l[5::]))