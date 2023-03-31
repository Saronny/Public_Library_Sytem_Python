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
    def __init__(self, title, userNumber, isbn):
        self.title = title
        self.isbn = isbn
        self.userNumber = userNumber
        self.status = "Available"
        self.returnDate = self.SetReturnDate()

    def getTitle(self):
        return self.title
    
    def getUserNumber(self):
        return self.userNumber
    
    def getDate(self):
        return self.date
    
    def getISBN(self):
        return self.isbn
    
    def setStatus(self, status):
        self.status = status
        
    def getStatus(self):
        return self.status
    
    def SetReturnDate(self):
        if self.status == "Available":
            self.returnDate = ""
        else:
            self.returnDate = datetime.date.today() + datetime.timedelta(days=14)
        
    def CalculateFine(self):
        today = datetime.date.today()
        if today > self.date:
            days = today - self.date
            return days.days * 10
        else:
            return 0
    
    
    