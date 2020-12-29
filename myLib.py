# Elise Merritt
#
# Library of functions for use in main program

#Function for determining if a given number is a Harshad number
def isHarshad(num):
    #Initializes variables needed for calculating sum of digits
    length=len(str(num))
    sum=0
    #Loop calculates sum of the digits in the number using casting to retrieve digits
    for i in range(0,length):
        curr_digit=int(str(num)[i])
        sum=sum+curr_digit
    #Determines if number is divisible by it's sum
    if num==0 or num%sum==0:
        return True
    else:
        return False

#Function for determining if a given number has a 7 in it's tens column
def isSiete(num):
    #Retrieves tens column digit of number
    if(len(str(num))<2):
        return False
    ten_column=int(str(num)[-2])
    #Checks if tens column digit is 7
    if ten_column==7:
        return True
    else:
        return False

#A constant
Hodges=14
