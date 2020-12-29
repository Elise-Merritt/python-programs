# Elise Merritt
#
# Creates a graph of unsorted and sorted random numbers

#Import matplotlib.pyplot for graphing
import matplotlib.pyplot as plt

#Read in data and sort it-from code submitted for assignment 4
infile=open("rands.txt", "r")
data=infile.read()
data=data.replace("\n", "\t")
data=data.replace(" ", "\t")
data=data.split("\t")
#convert list into list of integers and sort it
sort_numlist=[]
for i in range(0, len(data)-1):
    sort_numlist.append(int(data[i]))
unsort_numlist=sort_numlist
sort_numlist.sort()

#Graph unsorted numbers
unsort=range(0, len(data)-1)
plt.plot(unsort, unsort_numlist)
plt.xlabel("Index")
plt.ylabel("Unsorted numbers")
plt.show()

#Graph sorted numbers
sort=range(0, len(data)-1)
plt.plot(sort, sort_numlist)
plt.xlabel("Index")
plt.ylabel("Sorted numbers")
plt.show()
