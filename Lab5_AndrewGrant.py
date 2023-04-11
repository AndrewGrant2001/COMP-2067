# Andrew Grant
# 105226219

# Program to compute and display the denominations of the coins that should be
# used to give that amount of change to the shopper.

# Getting the input from the user
numCents = int(input("Enter the number of cents to make change for: "))

# Changing Toonies
numToonies = numCents // 200;
numCents = numCents % 200;

# Changing Loonies
numLoonies = numCents // 100;
numCents = numCents % 100;

# Changing Quarters
numQuarters = numCents // 25;
numCents = numCents % 25;

# Changing Dimes
numDimes = numCents // 10;
numCents = numCents % 10;

# Changing Nickels
numNickels = numCents // 5;
numCents = numCents % 5;

# Outputting the information
print(f'''The number of toonies: {numToonies}
The number of loonies: {numLoonies}
The number of quarters: {numQuarters}
The number of dimes: {numDimes}
The number of nickels: {numNickels}
The number of cents: {numCents}
''')






