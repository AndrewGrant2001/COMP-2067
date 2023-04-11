# Andrew Grant
# 105226219

# Program to compute the Accumulated Value using interest rate, compounding period, term, and principal value.

# Input/Processing Part 1
P = 1000  # Declaring/creating variable
n = 1  # Declaring/creating variable
r = 0.06  # Declaring/creating variable
t = 10  # Declaring/creating variable
A = 0  # Declaring/creating variable

A = P * ((1 + (r / n)) ** (n * t))  # Calculating Accumulated Value

# Output Part 1
print(f'''
Principal-Value | Times-Interest-Compounded | Annual-Int-Rate | Term | Accumulated Value
----------------------------------------------------------------------------------------
      {P}                  {n}                       {r * 100.0:.2f}%        {t}        {A:.2f}''')

# Input/Processing Part 2
P = 2000  # Setting new value
n = 2  # Setting new value
r = 0.032  # Setting new value
t = 15  # Setting new value

A = P * ((1 + (r / n)) ** (n * t))  # Calculating Accumulated Value

# Output Part 2
print(
    f'''      {P}                  {n}                       {r * 100.0:.2f}%        {t}        {A:.2f}''')

# Input/Processing Part 3
P = 3000
n = 4
r = 0.0925
t = 10

A = P * ((1 + (r / n)) ** (n * t))  # Calculating Accumulated Value

# Output Part 3
print(
    f'''      {P}                  {n}                       {r * 100.0:.2f}%        {t}        {A:.2f}''')
