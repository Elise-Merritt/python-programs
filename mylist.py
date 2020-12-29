# Elise Merritt
#
# Calculates the average of the negative numbers in a list

#Initializes list and variables used to keep track of list position and values needed to calculate average
MyList = [ 23, -45, 6, -23, -9, 77, 54, -54, 21, -2, 8, -3, -23, 45, 93, -43, 999, -2, 3, 78, 90 ]
i=0
size=0
curr=MyList[i]
sum=0
#Loops through list until 999 is reached
while(curr!=999):
    #Checks if number is negative, then adds to values needed for average as necessary
    if(curr<0):
        sum=sum+curr
        size=size+1
    #Moves forward in list
    i=i+1
    curr=MyList[i]
#Calculates and prints average of negative numbers in list
avg=sum/size
print(avg)

    
    
