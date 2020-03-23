from operator import mul
import random
total=0
incs = []
mistakes = False
qs=int(input("Number of questions:"))
for num in range(0, qs):
    x=random.randint(6, 8)    
    y=random.randint(13, 20)
    print("What is " + str(x) + " x " +str(y)+ "?")
    answer=int(input("Your Answer:"))
    if answer == (mul(x, y)):
        print("Correct!")
        total=total+1
    elif answer == (000):
        exit()
    else:
        print("Wrong, the answer is " + str(x*y))
        mistakes = True
        incs.append("You said "+ str(x) + " times " +str(y)+" = " +str(answer)+ " but the answer is actually "+str(mul(x, y)))
print("You got "+str(total)+" out of "+str(qs)+" questions correct!")
if mistakes == True:
    print("Here are your mistakes:")
    z = 0
    for num in range(0, len(incs)):
        print(incs[z])
        z+=1
