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

    def setAuthor(self, author):
        self.author = author

    def setCountry(self, country):
        self.country = country

    def setImageLink(self, imageLink):
        self.imageLink = imageLink

    def setLink(self, link):
        self.link = link

    def setPages(self, pages):
        self.pages = pages

    def setTitle(self, title):
        self.title = title

    def setISBN(self, ISBN):
        self.ISBN = ISBN

    def setYear(self, year):
        self.year = year


class BookItem:
    def __init__(self, title, userNumber, isbn):
        self.title = title
        self.isbn = isbn
        self.userNumber = userNumber
        self.status = "Available"
        self.returnDate = ""

    def getTitle(self):
        return self.title

    def getUserNumber(self):
        return self.userNumber

    def getDate(self):
        return self.returnDate

    def getISBN(self):
        return self.isbn

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def setUserNumber(self, userNumber):
        self.userNumber = userNumber

    def setReturnDate(self):
        self.returnDate = str(datetime.date.today() +
                              datetime.timedelta(days=60))

    def setReturnDateNull(self):
        self.returnDate = ""

    def setISBN(self, isbn):
        self.isbn = isbn

    def setTitle(self, title):
        self.title = title

    def CalculateFine(self):
        today = datetime.date.today()
        if today > self.date:
            days = today - self.date
            return days.days * 10
        else:
            return 0
