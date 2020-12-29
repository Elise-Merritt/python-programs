#Elise Merritt
#
#Main program of final project

#Load needed libraries
from finalproj_library import *
from random import shuffle

#Read in data of all books it's possible to search, and creates needed data structures, output file
already_read=Stack([])
all_books=[]
infile=open("good_reads_data.csv", encoding="utf8", mode='r', newline='')
outfile=open("search_output.txt", encoding="utf8", mode='w')
data1=infile.read()
data2=data1.split("^\r\n")
for book in data2[1:]:
    book=book.replace("\r\n", "")
    book_data=book.split(",")
    if book_data==['']:
        pass
    else:
        new_book=Book(book_data[0],book_data[1],book_data[2],book_data[3],book_data[4],book_data[5].strip(),book_data[6],book_data[7],book_data[8],book_data[9],book_data[10],book_data[11])
        all_books.append(new_book)

#Run main search
keep_going=True
while(keep_going==True):
    first_choice=int(input("Press 1 to retrieve the last book you searched for and 2 to pick a new one."))
    #Using stack, retrieves last book user searched for
    if first_choice==1:
        if already_read.isEmpty()==True:
            print("You haven't read any books yet!")
        else:
            last_book=already_read.pop()
            print("You last read", last_book.getTitle(), "by", last_book.getAuthor())
            already_read.push(last_book)
    else:
        #Searches for books using user-determined parameters
        print("You can search for books to read by author's average rating, author name, author's rating count, author's review count, book's average rating, book title, book genre (up to 2), book's number of ratings, book's number of reviews, book's number of pages, and the book's score.")
        second_choice=int(input("Enter 1 to input search parameters using a text file and 2 to input search parameters using the console."))
        #User selects search parameters and ranking metric using input file
        if second_choice==1:
            fname=str(input("Enter the file name."))
            books_selected=[]
            ranking=0
            with open(fname, mode='r') as f:
                for line in f:
                    fsearch=line.split(",")
                    if len(fsearch)==1:
                        ranking=int(fsearch[0].strip("\n"))
                    elif len(books_selected)==0:
                        books_selected=search(int(fsearch[0]),str(fsearch[1].strip("\n")),all_books)
                    else:
                        books_selected=search(int(fsearch[0]),str(fsearch[1].strip("\n")),books_selected)
            f.close()
            if ranking==0:
                shuffle(books_selected)
                if len(books_selected)==0:
                    print("No books matched your selection.")
                else:
                    book_picked=books_selected[0]
                    print(book_picked.getTitle(),"by",book_picked.getAuthor())
                    already_read.push(book_picked)
                    for j in books_selected:
                        currline=j.getTitle()+" by "+j.getAuthor()+"\n"
                        outfile.write(currline)
            else:
                if len(books_selected)==0:
                    print("No books matched your selection.")
                else:
                    books_chosen=sort(ranking, books_selected)
                    book_picked=books_chosen[0]
                    print(book_picked.getTitle(),"by",book_picked.getAuthor())
                    already_read.push(book_picked)
                    for k in books_chosen:
                        currline=k.getTitle()+" by "+k.getAuthor()+"\n"
                        outfile.write(currline)
            
        else:
            #User selects search parameters and ranking metric using console
            third_choice=int(input("How many terms do you want to search by?"))
            books_selected=[]
            for i in range(0,third_choice):
                fourth_choice=int(input("Enter 1 to search by author's minimum average rating, 2 to search by author name, 3 to search by author's minimum rating count, 4 to search by author's minimum review count, 5 to search by book's minimum average rating, 6 to search by book title, 7 to search by book genre (can be entered twice), 8 to search by book's minimum number of ratings, 9 to search by book's minimum number of reviews, 10 to search by book's maximum number of pages, and 11 to search by book's minimum score."))
                fifth_choice=str(input("Enter the search term, for example the title of the book if you chose 6."))
                if i==0:
                    books_selected=search(fourth_choice, fifth_choice, all_books)
                else:
                    books_selected=search(fourth_choice, fifth_choice, books_selected)
            print("If you choose to rank the selected books by a parameter, the highest-ranking book will be selected. If not, a randomly selected book will be displayed.")
            sixth_choice=int(input("Enter 0 to not rank the selected books, 1 to rank by author's average rating, 2 to rank by author's rating count, 3 to rank by author's review count, 4 to rank by book's average rating, 5 to rank by book's number of ratings, 6 to rank by book's number of reviews, 7 to rank by book's number of pages, and 8 to rank by the book's score."))
            if sixth_choice==0:
                shuffle(books_selected)
                if len(books_selected)==0:
                    print("No books matched your selection.")
                else:
                    book_picked=books_selected[0]
                    print(book_picked.getTitle(),"by",book_picked.getAuthor())
                    already_read.push(book_picked)
                    for j in books_selected:
                        currline=j.getTitle()+" by "+j.getAuthor()+"\n"
                        outfile.write(currline)
            else:
                if len(books_selected)==0:
                    print("No books matched your selection.")
                else:
                    books_chosen=sort(sixth_choice, books_selected)
                    book_picked=books_chosen[0]
                    print(book_picked.getTitle(),"by",book_picked.getAuthor())
                    already_read.push(book_picked)
                    for k in books_chosen:
                        currline=k.getTitle()+" by "+k.getAuthor()+"\n"
                        outfile.write(currline)
    #User decides when to stop searching for books
    last_choice=int(input("Press 1 to search again and 2 to exit."))
    if last_choice==1:
        keep_going=True
    else:
        keep_going=False

infile.close()                
outfile.close()
