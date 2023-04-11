# Andrew Grant
# 105226219
# Program to ask the user for their birth month and day and return their zodiac sign.

# Welcome Message
print("Welcome to the Zodiac Calculator!")

# getting the inputs
month = int(input("Please enter your month of birth as a number: "))
day = int(input("Please enter your day of birth as a number: "))

# if blocks to catch error and/or identify and print their zodiac sign
if month < 1 or month > 12 or day < 1 or day > 31:
    print("You have an invalid input.")
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("You are a Capricorn")
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("You are a Aquarius")
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print("You are a Pisces")
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("You are a Aries")
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("You are a Taurus")
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    print("You are a Gemini")
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    print("You are a Cancer")
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("You are a Leo")
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("You are a Virgo")
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    print("You are a Libra")
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    print("You are a Scorpio")
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("You are a Sagittarius")
else:
    print("Please try again")
