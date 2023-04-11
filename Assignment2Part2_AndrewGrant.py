# Andrew Grant
# 105226219
# Program to identify the type of triangle given the three side lengths

# getting the input from the user
side1 = int(input("Enter the first side length: "))
side2 = int(input("Enter the second side length: "))
side3 = int(input("Enter the third side length: "))

# if statements to catch error and/or output the type of triangle
if side1 < 0 or side1 > 100 or side2 < 0 or side2 > 100 or side3 < 0 or side3 > 100:
    print("You have at least one invalid input. Side lengths should be between 0 and 100.")
elif side1 == side2 and side2 == side3:
    print("This is an equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("This is an isosceles triangle.")
else:
    print("This is an scalene triangle.")
