s,c = input("Enter string : "),0
for i in range(len(s)):
    if s[i] != s.lower()[i]:c+=1
print("No. of uppercase letters :",c)