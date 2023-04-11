# Andrew Grant
# 105226219
# Program to calculate the number of dog years given a positive integer

while True:
    years = int(input("Please enter the age of a dog in human years (-1 to exit): "))

    if years == -1:
        break # As per profs email for exit case
    elif years <= 0:
        print("Please enter a positive integer.") # Catches wrong inputs
    elif years <= 2:
        print(f'''The dog is {years * 10.5} years old in dog years''') # if input is less than two years
    else:
        print(f'''The dog is {((years - 2) * 4) + 21} years old in dog years''') # if input is more than two years
