print("This program converts temperatures from Celsius, Fahrenheit, and Kelvin. Below are your options:")
print("Celsius to Fahrenheit")
print("Fahrenheit to Celsius")
print("Celsius to Kelvin")
print("Kelvin to Celsius")
print("Fahrenheit to Kelvin")
print("Kelvin to Fahrenheit")
def ctof(c):
    f=c*9/5+32
    return f
def ftoc(f):
    c=(f-32)*5/9
    return c
def ctok(c):
    k=c+273.15
    return k
def ktoc(k):
    c=k-273.15
    return c
def ftok(f):
    k=(f+459.67)*5/9
    return k
for num in range(0, 40):
    conversion=input("What conversion do you want?:")
    if conversion==("Celsius to Fahrenheit"):
        x=input("Put in degrees Celsius number:")
        x=int(x)
        print(ctof(x))
    elif conversion==("Fahrenheit to Celsius"):
        y=input("Put in degrees Fahrenheit number:")
        y=int(y)
        print(ftoc(y))
    elif conversion==("Celsius to Kelvin"):
        z=input("Put in degrees Celsius number:")
        z=int(z)
        print(ctok(z))
    elif conversion==("Kelvin to Celsius"):
        a=input("Put in Kelvin number:")
        a=int(a)
        print(ktoc(a))
    elif conversion==("Fahrenheit to Kelvin"):
        b=input("Put in degrees Fahrenheit number:")
        b=int(b)
        print(ftok(b))
    elif conversion==("Kelvin to Fahrenheit"):
        c=input("Put in Kelvin number:")
        c=int(c)
        print(ktof(c))
    else:
        print("Invalid!")
