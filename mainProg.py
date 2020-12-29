# Elise Merritt
#
# Program that processes numbers in a file using myLib contents

#import contents of myLib library
from myLib import isHarshad, isSiete, Hodges

#Open input file and retrieve contents
infile=open("Rumbers.txt", "r")
data=infile.read()
data=data.replace("\n", "\t")
data=data.split("\t")
#Open output file and initialize needed variables
output=open("HarshOut.txt", "w")
sum=0
#Loop through file contents and process them using myLib contents
for i in data:
    curr_num=int(i)
    if(isHarshad(curr_num)==True):
        sum=sum+curr_num
    if(isHarshad(curr_num)==True and isSiete(curr_num)==True):
        output.write(str(curr_num)+",")
    if(isHarshad(curr_num)==True and isSiete(curr_num)==True and curr_num%Hodges==True):
        print(curr_num)
print("The sum of the Harshad number is", sum)
#Close files
infile.close()
output.close()
