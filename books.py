import datetime

class Book:
    def __init__(self, author, country, imageLink, link, pages, title, ISBN, year):
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.link = link
        self.pages = pages
        self.title = title
        self.ISBN = ISBN
        self.year = year

    def getAuthor(self):
        return self.author
    
    def getCountry(self):
        return self.country
    
    def getImageLink(self):
        return self.imageLink
    
    def getLink(self):
        return self.link
    
    def getPages(self):
        return self.pages
    
    def getTitle(self):
        return self.title
    
    def getISBN(self):
        return self.ISBN
    
    def getYear(self):
        return self.year
    


class BookItem:
    def __init__(self, title, user):
        self.title = title
        self.user = user
        self.returnDate = datetime.date.today() + datetime.timedelta(days=30)

    def getBook(self):
        return self.book
    
    def getUser(self):
        return self.user
    
    def getDate(self):
        return self.date
        
    def CalculateFine(self):
        today = datetime.date.today()
        if today > self.date:
            days = today - self.date
            return days.days * 10
        else:
            return 0
    
    
    