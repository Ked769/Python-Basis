s = input("Enter string : ")
if s[::-1].lower() == s.lower():print(f"{s} is a palindrome.")
else:print(f"{s} is not a palindrome.")