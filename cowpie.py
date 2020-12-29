# Elise Merritt
#
# A program that prints natural numbers from 1 to 100, substituting those divisible by 3 and/or 7

#Retrieves all numbers from 1 to 100, exclusive
for i in range(1, 101):
    #Prints "Cow", "Pie" or "CowPie" if numbers are divisible by 3, 7, or both
    if(i%3==0 and i%7==0):
        print("CowPie")
    elif(i%3==0):
        print("Cow")
    elif(i%7==0):
        print("Pie")
    #If number isn't divisible by 3 or 7, it is printed
    else:
        print(i)
