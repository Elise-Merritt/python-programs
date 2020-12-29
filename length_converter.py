# Author: Elise Merritt
#
# A program to output length conversions


#Retrieves number of inches from input
num_inches=int(input("Please enter the number of inches: "))

#Converts inches to feet, then prints result
num_feet=int(num_inches/12) 
print(num_feet, "feet")

#Converts feet to yards, then prints result
num_yards=int(num_feet/3)
print(num_yards, "yards")

#Converts yards to miles, then prints result
num_miles=int(num_yards/1760)
print(num_miles, "miles")


