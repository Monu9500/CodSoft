print(" Select operation: ['+'==Add], ['-'==Subtract], ['*'==Multiply] and ['/'==Divide]" )

choice = input(" Enter operation [+,-,*,/]: ")

if choice in ('+', '-', '*', '/'):
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if choice == '+':
        print(n1, "+", n2, "=", (n1+n2))
    elif choice == '-':
        print(n1, "-", n2, "=", (n1-n2))
    elif choice == '*':
        print(n1, "*", n2, "=", (n1*n2))
    elif choice == '/':
        if n2 == 0:
            print("Error.")
        else:
            print(n1, "/", n2, "=",(n1/n2))
else:
    print("Enter a valid input.")