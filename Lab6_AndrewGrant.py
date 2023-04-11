# Andrew Grant
# 105226219

# Program to calculate the oil price based on the order amount

# Variables defined to hold the input and output values
order = 0
cost = 0

# Getting the input from the user
order = int(input("Amount of oil is? "))

# Calculate the cost based on the amount of oil being purchased
if order < 150:
    cost = order * 2.25
elif order < 250:
    cost = (150 * 2.25) + (order - 150) * 2.10
else:
    cost = (150 * 2.25) + (100 * 2.10) + (order - 250) * 1.99

# Outputting the cost to the user
print(f'''The cost of the oil is {cost}''')