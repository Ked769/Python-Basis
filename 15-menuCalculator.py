while True:    
    n = int(input(\
        "\nEnter number to choose operation:\n1 for +, 2 for -, 3 for *, 4 for /\n5 for //, 6 for %, 7 for **, 8 for append : "))
    a,b = float(format(float(input("\nEnter first number : ")),'.12g')), float(format(float(input("\nEnter second number : ")),'.12g'))
    print()
    try:
        print([0,"a+b","a-b","a*b","a/b","a//b","a%b","a**b",str(a)+" str+ "+str(b)][n], "=", [0,a+b,a-b,a*b,a/b,a//b,a%b,a**b,str(a)+str(b)][n])
        if not int(input("\nEnter 1 for another calculation, else enter 0 : ")):
            break
    except OverflowError:
        print("Sorry, numbers too large. Try again!\n")
    except IndexError:
        print(f"Please re-enter your choice, {n} is not valid!")
    except TypeError:
        print(f"Please re-enter your choice, {n} is not valid!")
