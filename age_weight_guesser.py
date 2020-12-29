# Elise Merritt
#
# A program that lets users guess an age and weight


#Intializes the age and weight variables
age=30
weight=136

#Gets guessed age and weight from input
age_guess=int(input("Enter your guess for age:"))
weight_guess=int(input("Enter your guess for weight:"))

#Checks if guessed age and weight are higher than actual age and weight
if(age_guess>age and weight_guess>weight):
    print("Both higher")
#Checks if guessed age and weight are lower than actual age and weight
elif (age_guess<age and weight_guess<weight):
    print("Both lower")
#Checks if guessed age and weight are actual age and weight
elif (age_guess==age and weight_guess==weight):
    print("Bingo")
#Prints "Game over" if none of above conditions are true
else:
    print("Game over")
