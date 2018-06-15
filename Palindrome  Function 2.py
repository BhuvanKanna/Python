def ToBinary(baseTen):
    binaryString = ""
    currentPowerOfTwo = HighestPowerOfTwo(baseTen)
    while currentPowerOfTwo >= 1:
      if baseTen >= pow(2, currentPowerOfTwo):
        binaryString += "1"
      else:
        binaryString += "0"
      baseTen = baseTen % pow(2, currentPowerOfTwo)
      currentPowerOfTwo -= 1
    return binaryString + str(baseTen)
def ispalindrome(x):
    isp= "yes"
    index1=0
    index2=len(x)-1
    for num in range(0,len(x)//2):
        if x[index1]!=x[index2]:
            print("")
            isp="No" 
        index1+=1
        index2-=1
    return isp
def HighestPowerOfTwo(u):
    r = 0
    if u < 2:
        return 0
    else:
        while u > 1:
            t =u % 2
            u = u-t
            r += 1
            u = u/2
        return r
myInt=0
for num in range(1, 100000000):
    if ispalindrome(str(num))== "yes" and ispalindrome(ToBinary(num))=="yes":
        print(num, "", ToBinary(num))
        myInt += num
print()
