print("select the Operation")
print("1 for Addition")
print("2 for subtraction")
print("3 for Multiplication")
print("4 for Division")

choice = int(input("Enter the Operator(1/2/3/4)"))
a = int(input("Enter the first number"))
b = int(input("enter the second number"))

if choice == 1:
    print("Addition of", a, "+", b, "=", a+b)
elif choice == 2:
    print("Subtraction of", a, "-", b, "=", a-b)
elif choice == 3:
    print("Multiplication of", a, "*", b, "=", a*b)
elif choice == 4:
    print("division of", a, "/", b, "=", a/b)
else:
    print("invalid Input")
