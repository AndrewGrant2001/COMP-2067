# Andrew Grant
# 105226219

# Program to calculate the wind chill index rounded to the nearest integer by taking the inputs
# of the wind speeds (in km/h) and the air temperature (in degrees Celcius)

# Asks user to input the temperature and it is stored in variable temp
temp = float(input('Enter the air temperature (in degrees Celcius): '))

# Asks user to input the wind and it is stored in variable wind
wind = float(input('Enter the wind speed (in km/h): '))

# Computes the chillIndex from the provided formula
chillIndex = 13.12 + (0.6215 * temp) - (11.37 * (wind ** 0.16)) + (0.3965 * temp * (wind ** 0.16))

# Outputs the chillIndex
print(f'''The windchill for {temp} degrees Celcius and {wind} km/h is: {round(chillIndex, 0):.0f}''')



