n=''
for i in input():
    if not ((65<=ord(i)<=91) or (97<=ord(i)<=123)):n+=i
    elif i.lower()==i:n+=i.upper()
    else: n+=i.lower()
print(n)