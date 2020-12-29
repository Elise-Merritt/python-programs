# Elise Merritt
#
# A program that recursively raises a number (x) to a power (y)

#define the recursive function
def myPow(x, y):
    #base case
    if(y==0):
        return 1
    #if not base case, call function again
    else:
        return x*myPow(x, y-1)

#test the recursive function
print(myPow(7, 3))
print(myPow(2, 6))
print(myPow(5, 5))
