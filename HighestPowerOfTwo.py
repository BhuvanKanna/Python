y=16
def ToBinary(y) :
    z = ""
    while y != 0 :
        z  =  str (y % 2) + z
        z    //=  2
    return z
print(ToBinary(y))

