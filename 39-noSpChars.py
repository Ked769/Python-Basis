c,s = 0,input("Enter string : ")
for i in s:
    if not i.isdigit() and not (65<ord(i) or ord(i)>123):c+=1
print("No. of special characters :",len(s)-c)