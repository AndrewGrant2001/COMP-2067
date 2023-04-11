# Andrew Grant
# 105226219

# Program to compute the sum of the digits of a number

# Obtaining the input from the user
num: int = int(input("Enter a number: "))

# Intializing a sum variable
sum = 0

# Loop to take the remainder and add it to the sum and then "chop" the ones digit from the number
# If the input was always four you could just repeat the inside of the loop code 4 times to do the same thing
# This functions for any size number
while (num > 0) :
    sum = sum + num % 10
    num = num // 10

# Outputting the sum
print(f'''The sum of the digits is equal to {sum}''')



