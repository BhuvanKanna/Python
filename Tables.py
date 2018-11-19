from operator import mul
import random
total=0
qs=int(input("Number of questions:"))
for num in range(0, qs):
    x=random.randint(9, 13)
    y=random.randint(13, 20)
    print("What is " + str(x) + " times " +str(y)+ "?")
    answer=int(input("What is your answer: "))
    if answer == (mul(y, x)):
        print("Correct!")
        total=total+1
    elif answer == (999):
        exit()
    else:
        print("Wrong, the answer is " + str(x*y))

