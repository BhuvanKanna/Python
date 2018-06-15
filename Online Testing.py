primary_color1 = input("Enter primary color:")
primary_color2 = input("Enter primary color:")

if (primary_color1 == "red" and primary_color2 == "blue") or (primary_color1 == "blue" and primary_color2 == "red"):
    print("When you mix red and blue, you get purple.")

elif (primary_color1 == "blue" and primary_color2 == "yellow") or (primary_color1 == "yellow" and primary_color2 == "blue"):
    print("When you mix blue and yellow, you get green.")

elif (primary_color1 == "yellow" and primary_color2 == "red") or (primary_color1 == "red" and primary_color2 == "yellow"):
    print("When you mix yellow and red, you get orange.")

else:
    print("You didn't input two primary colors.")



    
