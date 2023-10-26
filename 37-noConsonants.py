n = list(''.join((input("Enter string : ").lower()).split()) )
print("No. of consonants : ", len(n)-(n.count("a")+n.count("e")+n.count("i")+n.count("o")+n.count("u")))