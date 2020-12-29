#Elise Merritt
#
#Library of classes and search functions

#import needed libraries
from operator import itemgetter, attrgetter

#Class defines author of a book
class Author:

    def __init__(self, auth_average_rating, name, rating_count, review_count):
        self.auth_average_rating=auth_average_rating
        self.name=name
        self.rating_count=rating_count
        self.review_count=review_count
    def getAuthAverageRating(self):
        return self.auth_average_rating
    def setAuthAverageRating(self, naverage_rating):
        self.auth_average_rating=naverage_rating
    def getAuthor(self):
        return self.name
    def setAuthor(self, nname):
        self.name=nname
    def getRatingCount(self):
        return self.rating_count
    def setRatingCount(self, nrating_count):
        self.rating_count=nrating_count
    def getReviewCount(self):
        return self.review_count
    def setReviewCount(self, nreview_count):
        self.review_count=nreview_count
    
#Class defines a book      
class Book(Author):
    
    def __init__(self, auth_average_rating, name, rating_count, review_count, average_rating, title, genre1, genre2, num_ratings, num_reviews, pages, score):
        Author.__init__(self, auth_average_rating, name, rating_count, review_count)
        self.average_rating=average_rating
        self.title=title
        self.genre1=genre1
        self.genre2=genre2
        self.num_ratings=num_ratings
        self.num_reviews=num_reviews
        self.pages=pages
        self.score=score
    def getAverageRating(self):
        return self.average_rating
    def setAverageRating(self, naverage_rating):
        self.average_rating=naverage_rating
    def getTitle(self):
        return self.title
    def setTitle(self, ntitle):
        self.title=ntitle
    def getGenre1(self):
        return self.genre1
    def setGenre1(self, ngenre1):
        self.genre1=ngenre1
    def getGenre2(self):
        return self.genre2
    def setGenre2(self, ngenre2):
        self.genre2=ngenre2
    def getNumRatings(self):
        return self.num_ratings
    def setNumRatings(self, nnum_ratings):
        self.num_ratings=nnum_ratings
    def getNumReviews(self):
        return self.num_reviews
    def setNumReviews(self, nnum_reviews):
        self.num_reviews=nnum_reviews
    def getPages(self):
        return self.pages
    def setPages(self, npages):
        self.pages=npages
    def getScore(self):
        return score
    def setScore(self, nscore):
        self.score=nscore

#Class defines a stack
class Stack:
    def __init__(self, data):
        self.data=data
    def push(self, item):
        self.data.append(item)
    def pop(self):
        return self.data.pop(len(self.data)-1)
    def isEmpty(self):
        if len(self.data)==0:
            return True
        else:
            return False

#Method used to filter books using specified search parameter and term
def search(num, search_term, books):
    output=[]
    if num==1:
        for i in books:
            if i.getAuthAverageRating()>=search_term:
                output.append(i)
            else:
                pass
    elif num==2:
        for i in books:
            if i.getAuthor()==search_term:
                output.append(i)
            else:
                pass
    
    elif num==3:
        for i in books:
            if i.getRatingCount()>=search_term:
                output.append(i)
            else:
                pass
    elif num==4:
        for i in books:
            if i.getReviewCount()>=search_term:
                output.append(i)
            else:
                pass
    elif num==5:
        for i in books:
            if i.getAverageRating()>=search_term:
                output.append(i)
            else:
                pass
    
    elif num==6:
        for i in books:
            if i.getTitle()==search_term:
                output.append(i)
            else:
                pass
    elif num==7:
        for i in books:
            if i.getGenre1()==search_term or i.getGenre2()==search_term:
                output.append(i)
            else:
                pass
    elif num==8:
        for i in books:
            if i.getNumRatings()>=search_term:
                output.append(i)
            else:
                pass
    elif num==9:
        for i in books:
            if i.getNumReviews()>=search_term:
                output.append(i)
            else:
                pass
    elif num==10:
        for i in books:
            if i.getPages()<=search_term:
                output.append(i)
            else:
                pass
    else:
        for i in books:
            if i.getScore()<=search_term:
                output.append(i)
            else:
                pass
    return output

#Method used to sort books based on rankings chosen by user
def sort(num, books):
    if num==1:
        output=sorted(books, key=attrgetter('auth_average_rating'), reverse=True) 
    elif num==2:
        output=sorted(books, key=attrgetter('rating_count'), reverse=True)
    elif num==3:
        output=sorted(books, key=attrgetter('review_count'), reverse=True)
    elif num==4:
        output=sorted(books, key=attrgetter('average_rating'), reverse=True)
    elif num==5:
        output=sorted(books, key=attrgetter('num_ratings'), reverse=True)
    elif num==6:
        output=sorted(books, key=attrgetter('num_reviews'), reverse=True)
    elif num==7:
        output=sorted(books, key=attrgetter('pages'), reverse=True)
    else:
        output=sorted(books, key=attrgetter('score'), reverse=True)
    return output
