import time
myTime=time.localtime()
x=(myTime.tm_hour)
x=int(x)
if x>12:
    x=x-12
    
y=(myTime.tm_min)
y=str(y)
z=(myTime.tm_sec)
z=str(z)
print(x+":"+y+":")
