def factorial(n):
    if n==1:
        return n
    return n*(factorial(n-1))
x=input("Put in a number:")
x=int(x)
print(factorial(x))                                                        




