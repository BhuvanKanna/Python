
print('Remember, capital letter at beginning and no spaces!!!')
print('                                         ')
_color1 = input("Enter  color 1:")
print('                  ')
y = input("Enter primary color 2:")

if (x == "Red" and y == "Blue") or (x == "Blue" and y == "Red"):
    print("When you mix red and blue, you get purple.")
elif (x == "Blue" and y == "Yellow") or (x == "Yellow" and y == "Blue"):
    print("When you mix blue and yellow, you get green.")
elif (x == "Yellow" and y == "Red") or (x == "Red" and y == "Yellow"):
    print("When you mix yellow and red, you get orange.")
else:
    print("You didn't input two primary colors,or you didn't follow the instructions. Please try again.")
print("Thank You!!:)")
