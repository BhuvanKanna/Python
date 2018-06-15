def ispalindrome(x):
    isp= "yes"
    index1=0
    index2=len(x)-1
    for num in range(0,len(x)//2):
        if x[index1]!=x[index2]:
            isp="no"
        index1+=1
        index2-=1
    return isp
x=input("Put in a string:")
print (ispalindrome(x))
