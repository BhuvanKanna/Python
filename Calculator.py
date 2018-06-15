x=input("Enter the first number:")
x=int(x)
y=input("Enter the second number:")
y=int(y)
operation=input("Enter the operation symbol:")
if operation==("+"):
        print(x+y)
if operation==("-"):
        print(x-y)
if operation==("/"):
        print(x*y)
if operation==("*"):
        print(x/y)
if operation==("**"):
        print(x**y)
if operation==("compare"):
    if x>y:
            x=str(x)
            y=str(y)
            print(x+" is greater than "+y)
    if x<y:
            x=str(x)
            y=str(y)
            print(x+" is less than "+y)
    if x==y:
            x=str(x)
            y=str(y)
            print(x+" is equal to "+y)

