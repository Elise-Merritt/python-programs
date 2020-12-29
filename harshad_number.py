# Elise Merritt
#
# A program that finds the Harshad numbers (numbers divisible by the sum of their digits) between 0 and 500

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

#Loop prints every Harshad number between 0 and 500
for i in range(0,501):
    if(isHarshad(i)==True):
        print(i)

