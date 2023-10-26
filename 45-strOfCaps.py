s,s1 = input("Enter string : "),[]
for i in s:
    if i!=i.lower() or i==" ":s1.append(i)
print("Capital letter string :",''.join(s1))