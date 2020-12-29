# Elise Merritt
#
# Program that searches for numbers in a file using binary and linear search

#import functions used to search
from mySearches import bsearch, lsearch

#open file with numbers and retrieve numbers as a list
infile=open("rands.txt", "r")
data=infile.read()
data=data.replace("\n", "\t")
data=data.replace(" ", "\t")
data=data.split("\t")
#convert list into list of integers and sort it
number_list=[]
for i in range(0, len(data)-1):
    number_list.append(int(data[i]))
number_list.sort()


#search through sorted list for numbers using binary and linear searches
print("Output of binary search for 78700 is "+str(bsearch(78700, number_list)))
print("Output of linear search for 78700 is "+str(lsearch(78700, number_list)))
print("Output of binary search for 3333 is "+str(bsearch(3333, number_list)))
print("Output of linear search for 3333 is "+str(lsearch(3333, number_list)))
print("Output of binary search for 1118 is "+str(bsearch(1118, number_list)))
print("Output of linear search for 1118 is "+str(lsearch(1118, number_list)))
#close input file
infile.close()
