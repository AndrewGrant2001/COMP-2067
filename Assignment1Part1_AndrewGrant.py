# Andrew Grant
# 105226219
# Program to calculate the number of vines you can plant given the length of the row, amount of space end-posts
# and the distance between each vine.

# Asks user to input the length of the row and store it in variable r
r = float(input('Enter the length of the row (in feet):'))

# Asks user to input the space taken up by an end-post and store it in variable e
e = float(input('Enter the amount of space (in feet), used by an end-post assembly:'))

# Asks user to input the space between each vine and store it in s
s = float(input('Enter the distance (in feet) between each vine:'))

# Calculating the number of vines
v = ((r - 2.0) * e) / s

# Outputing the number of vines
print(f'''You have enough space for {v} vines.''')

