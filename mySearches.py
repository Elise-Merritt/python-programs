# Elise Merritt
#
# Library with two search functions, binary and linear search

#Function uses binary search algorithm to find the index of a number (x)
#in a list of numbers (num_list)
def bsearch(x, num_list):
    #initializes needed variables for search
    answer=0
    low=0
    high=len(num_list)-1
    lookups=0
    #search through list for number
    while low<=high:
        #halve amount of numbers to search through
        mid=(low+high)//2
        item=num_list[mid]
        #check if number is found-if not, intialize next search
        if x==item:
            lookups=lookups+1
            print("Binary Search Lookups to find " + str(x)+": "+str(lookups))
            return mid
        elif x<item:
            high=mid-1
            lookups=lookups+1
        else:
            low=mid+1
            lookups=lookups+1
    #if here, number is not in list
    print("Binary Search Lookups to find " + str(x)+": "+str(lookups))
    return -1

#Function uses linear search algorithm to find the index of a number (x)
#in a list of numbers (num_list)
def lsearch(x, num_list):
    lookups=0
    #search through list for number
    for i in range(0, len(num_list)-1):
        #check if number has been found
        if x==num_list[i]:
            lookups=lookups+1
            print("Linear Search Lookups to find " + str(x)+": "+str(lookups))
            return i
        else:
            lookups=lookups+1
    #if here, number is not in list
    print("Linear Search Lookups to find " + str(x)+": "+str(lookups))
    return -1


