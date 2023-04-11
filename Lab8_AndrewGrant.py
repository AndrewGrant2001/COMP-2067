# Andrew Grant
# 105226219
# Program to inform the user of what movie ratings they can see and the price.

# Welcome message
print(f'''Welcome to the Movie Calculator! (If you enter invalid inputs the program may crash or give inaccurate results)''')

check = "Yes"

# loop to run until they wish to exit
while check == "Yes":
    # getting the input/information from user
    age = int(input("Enter your age: "))
    withP = (input("Are you with your parents (Yes or No): ")).title()
    student = input("Are you a student (Yes or No): ").title()
    money = float(input("How much can you spend: "))

    print(f'''
    Determining your information...''')

    # if statements to output movie types they can see
    if age < 13 and withP == "Yes":
        print("Movie Types: G, PG")
    elif age < 13 and withP == "No":
        print("Movie Types: G")
    elif 13 <= age < 16 and withP == "Yes":
        print("Movie Types: G, PG, R")
    elif 13 <= age < 16 and withP == "No":
        print("Movie Types: G, PG")
    elif age >= 16:
        print("Movie Types: G, PG, R")
    else:
        print("You have entered something wrong. Please try again.")
    costM = 0 # setting the matinee cost to 0
    costE = 0 # setting the evening cost to 0

    # if statements to calculate cost
    if student == "Yes":
        costM = 4
        costE = 4
    elif student == "No":
        costM = 4.5
        costE = 6.5
    if withP == "Yes":
        costM += 4.5
        costE += 6.5

    # if statements to determine which show times they can attend
    if money - costM >= 0 and money - costE >= 0:
        print("Show Times: Matinee, Evening \n")
    elif money - costM >= 0:
        print("Show Times: Matniee \n")
    elif money - costE >= 0:
        print("Show Times: Evening \n")
    else:
        print("You don't have enough money to attend any movies \n")

    # to check if they want to continue
    check = input("Would you like to continue? (Yes to continue): ").title()
