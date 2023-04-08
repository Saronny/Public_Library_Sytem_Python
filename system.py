import json
import csv
import persons
import time
import books
import shutil
import os
import random
import string


class System:
    def __init__(self) -> None:
        self.users = []
        self.books = []
        self.bookItems = []
        self.loadUsers()
        self.loadBooks()
        self.loadBookItems()

    def loadUsers(self):
        if not os.path.exists('Data'):
            os.makedirs('Data')
        try:
            with open('Data/Members.csv') as f:
                reader = csv.reader(f, delimiter=';', quotechar="'")
                num = 0
                for row in reader:
                    self.users.append(persons.User(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[9]))
                    self.users[num].setPassword(row[8])
                    num += 1
        except:
            with open('Data/Members.csv', 'w', newline='') as f:
                writer = csv.writer(f, delimiter=';', quotechar="'")
                writer.writerow(["Number", "GivenName", "SurName", "StreetAddress", "ZipCode",
                                "City", "EmailAddress", "Username", "Password", "TelephoneNumber"])

    def loadBooks(self):
        try:
            with open('Data/Books.json') as f:
                data = json.load(f)
                for book in data:
                    self.books.append(books.Book(book["author"], book["country"], book["imageLink"],
                                      book["link"], book["pages"], book["title"], book["ISBN"], book["year"]))
        except:
            with open('Data/Books.json', 'w') as f:
                json.dump([], f)

    def getCurrentUser(self):
        return self.currentUser

    def getBooks(self):
        return self.books

    def getBook(self, query):
        for book in self.books:
            if book.getISBN() == query or book.getTitle() == query:
                return book
        return None

    def getUsers(self):
        return self.users

    def register(self, GivenName, SurName, StreetAddress, ZipCode, City, EmailAddress, Username, Password, TelephoneNumber):
        if Username == "" or Password == "":
            return "Username or password cannot be empty"
        for user in self.users:
            if user.getUsername() == Username:
                return "Username already taken"
        for char in Username:
            if char.isupper():
                return "Username cannot contain capital letters"

        Number = len(self.users) + 1
        newUser = persons.User(Number, GivenName, SurName, StreetAddress,
                               ZipCode, City, EmailAddress, Username, TelephoneNumber)
        newUser.setPassword(Password)
        self.users.append(newUser)
        self.saveUsers()

        return "User registered"

    def AddBook(self, author, country, imageLink, link, pages, title, ISBN, year):
        for book in self.books:
            if book.getISBN() == ISBN:
                return "Book already exists"
        newBook = books.Book(author, country, imageLink,
                             link, pages, title, ISBN, year)
        self.books.append(newBook)
        self.saveBooks()
        self.addBookItem(title, 0, ISBN)
        return "Book added"

    def saveUsers(self):
        try:
            with open('Data/Members.csv', 'w', newline='') as f:
                writer = csv.writer(f, delimiter=';', quotechar="'")
                for user in self.users:
                    writer.writerow([user.getNumber(), user.getName(), user.getSurname(), user.getAddress(), user.getZipcode(
                    ), user.getCity(), user.getEmail(), user.getUsername(), user.getPassword(), user.getTelephone()])
        except:
            print("Error saving users")

    def saveBooks(self):
        try:
            with open('Data/books.json', 'w') as f:
                json.dump([ob.__dict__ for ob in self.books], f)
        except:
            print("Error saving books")

    def removeBook(self, ISBN):
        try:
            self.removeBookItem(ISBN)
            for book in self.books:
                if book.getISBN() == ISBN:
                    self.books.remove(book)
                    self.saveBooks()
                    return "Book removed"
            return "Book not found"
        except:
            return "Error removing book"

    def search(self, req):
        try:
            r = []
            count = 0
            for book in self.books:
                if (req in book.getTitle() or req.capitalize() in book.getTitle()):
                    r.append(book)
                    count += 1
                elif (req in book.getAuthor() or req.capitalize() in book.getAuthor()):
                    r.append(book)
                    count += 1
            if (count == 0):
                return "No results found"
            return r
        except:
            return "Error loading books"

    def loadBookItems(self):
        try:
            with open('Data/BookItems.json') as f:
                data = json.load(f)
                for bookItem in data:
                    self.bookItems.append(books.BookItem(
                        bookItem["title"], bookItem["userNumber"], bookItem["isbn"]))

        except:
            try:
                with open('Data/BookItems.json', 'w') as f:
                    for book in self.books:
                        for i in range(5):
                            self.bookItems.append(books.BookItem(
                                book.getTitle(), 0, book.getISBN()))
                    json.dump([ob.__dict__ for ob in self.bookItems], f)
            except:
                print("Error creating book items")

    def getBookAvailable(self, title):
        try:
            count = 0
            for bookItem in self.bookItems:
                if bookItem.getTitle() == title and bookItem.getStatus() == "Available":
                    count += 1
            return count
        except:
            return "Error loading book items"

    def addBookItem(self, title, userNumber, isbn):
        for i in range(5):
            self.bookItems.append(books.BookItem(title, userNumber, isbn))
        self.saveBookItems()

    def saveBookItems(self):
        try:
            with open('Data/BookItems.json', 'w') as f:
                json.dump([ob.__dict__ for ob in self.bookItems], f)
        except:
            time.sleep(1)
            print("Error saving book items")

    def removeBookItem(self, isbn):
        try:
            for bookItem in self.bookItems:
                if bookItem.getISBN() == isbn:
                    self.bookItems.remove(bookItem)
            self.saveBookItems()
        except:
            return "Error removing book item"

    def getMembers(self):
        if self.users == []:
            return "No members found"
        return self.users

    def lendBook(self, query, userQuery):
        try:
            for i in userQuery:
                if i.isdigit() == True:
                    member = self.getMember(userQuery)
                    break
                else:
                    member = self.getMemberByUser(userQuery)
                    break
            if member == "Member not found":
                return "Member not found"
            userNumber = member.getNumber()
            loanedBooks = self.getLoanedBooks(userNumber)
            for book in loanedBooks:
                if book.getISBN() == query or book.getTitle() == query:
                    return "Member has already lent this book"
            count = 0
            for bookItem in self.bookItems:
                if bookItem.getUserNumber() == int(userNumber):
                    count += 1
            if count >= 3:
                return "Member has already lent 3 books"
            for bookItem in self.bookItems:
                if bookItem.getStatus() == "Lent":
                    continue
                if bookItem.getTitle() == query or bookItem.getISBN() == query and bookItem.getStatus() == "Available":
                    bookItem.setStatus("Lent")
                    bookItem.setUserNumber(int(userNumber))
                    bookItem.setReturnDate()
                    self.saveBookItems()
                    return "Book lent"
            return "No books available"
        except:
            return "Error lending book"

    def getMember(self, userNumber):
        try:
            for user in self.users:
                if user.getNumber() == userNumber:
                    return user
            return "Member not found"
        except:
            return "Error loading Members"

    def getMemberUsername(self, userNumber):
        try:
            for user in self.users:
                if user.getNumber() == userNumber:
                    return user.getUsername()
            return "Member not found"
        except:
            return "Error loading Members"

    def getMemberByUser(self, username):
        try:
            for user in self.users:
                if user.getUsername() == username:
                    return user
            return "Member not found"

        except:
            return "Error loading Members"

    def getLoanedBooks(self, query):
        try:
            books = []
            for i in query:
                if i.isdigit() == True:
                    userNumber = query
                    break
                else:
                    userNumber = self.getMemberByUser(query).getNumber()
                    break
            for bookItem in self.bookItems:
                if bookItem.getUserNumber() == int(userNumber):
                    books.append(bookItem)
            return books
        except:
            return "Error loading books"

    def returnBook(self, query, userNumber):
        try:
            for bookItem in self.bookItems:
                if bookItem.getTitle() == query or bookItem.getISBN() == query and bookItem.getUserNumber() == int(userNumber):
                    bookItem.setStatus("Available")
                    bookItem.setUserNumber(0)
                    bookItem.setReturnDateNull()
                    self.saveBookItems()
                    return "Book returned"
            return "Book not found"
        except:
            return "Error returning book"

    def getAllLoanedBooks(self):
        try:
            books = []
            for bookItem in self.bookItems:
                if bookItem.getStatus() == "Lent":
                    books.append(bookItem)
            return books
        except:
            return "Error loading books"

    def removeMember(self, query):
        try:
            for user in self.users:
                if user.getNumber() == query or user.getUsername() == query:
                    self.users.remove(user)
                    self.saveUsers()
                    return "Member removed"
            return "Member not found"
        except:
            return "Error removing member"

    def removeBook(self, query):
        try:
            if self.getBookAvailable(query) != 5:
                return "Book cannot be removed because it is currently lent"
            exists = False
            for book in self.books:
                if book.getTitle() == query or book.getISBN() == query:
                    exists = True
                    break
            if exists == False:
                return "Book not found"
            for bookItem in self.bookItems:
                if bookItem.getTitle() == query:
                    self.bookItems.remove(bookItem)
                if bookItem.getISBN() == query:
                    self.bookItems.remove(bookItem)
                else:
                    continue
            self.saveBookItems()
            for book in self.books:
                if book.getTitle() == query or book.getISBN() == query:
                    self.books.remove(book)
            self.saveBooks()
            return "Book removed"
        except:
            return "Error removing book"

    def editMember(self, query, option, new):
        try:
            for user in self.users:
                if user.getUsername() == query or user.getNumber() == query:
                    if option == 1:
                        for user in self.users:
                            if user.getUsername() == new:
                                return "Username already exists"
                        for i in new:
                            if i.isupper() == True:
                                return "Username cannot contain capital letters"
                        user.setUsername(new)
                        break
                    elif option == 2:
                        user.setPassword(new)
                        break
                    elif option == 3:
                        user.setAddress(new)
                        break
                    elif option == 4:
                        user.setTelephone(new)
                        break
                    elif option == 5:
                        user.setEmail(new)
                        break
                    elif option == 6:
                        user.setCity(new)
                        break
                    elif option == 7:
                        user.setGivenName(new)
                        break
                    elif option == 8:
                        user.setSurname(new)
                        break
                    elif option == 9:
                        user.setZipCode(new)
                        break
                    else:
                        return "Invalid option"
            self.saveUsers()
            return "Member edited"
        except:
            return "Member not found"

    def editBook(self, query, option, new):
        try:
            if self.getBookAvailable(query) != 5:
                return "Book cannot be edited because it is currently lent"
            for book in self.books:
                if book.getTitle() == query or book.getISBN() == query:
                    if option == 1:
                        for book in self.books:
                            if book.getTitle() == new:
                                return "Title already exists"
                        book.setTitle(new)
                        break
                    elif option == 2:
                        book.setAuthor(new)
                        break
                    elif option == 3:
                        for book in self.books:
                            if book.getISBN() == new:
                                return "ISBN already exists"
                        book.setISBN(new)
                        break
                    elif option == 4:
                        book.setLink(new)
                        break
                    elif option == 5:
                        book.setCountry(new)
                        break
                    elif option == 6:
                        try:
                            new = int(new)
                            book.setYear(new)
                        except:
                            return "Invalid year"
                        break
                    elif option == 7:
                        try:
                            new = int(new)
                            book.setPages(new)
                        except:
                            return "Invalid number of pages"
                        break
                    elif option == 8:
                        book.setImageLink(new)
                        break
                    else:
                        return "Invalid option"
            if option == 1 or option == 3:
                for bookItem in self.bookItems:
                    if bookItem.getTitle() == query:
                        bookItem.setTitle(new)
                        continue
                    if bookItem.getISBN() == query:
                        bookItem.setISBN(new)
                        continue
            self.saveBookItems()
            self.saveBooks()
            return "Book edited"
        except:
            return "Book not found"

    def generateSerial(self):
        serial = ""
        for i in range(6):
            serial += random.choice(string.ascii_letters + string.digits)
        return serial

    def makeBackUp(self):
        try:
            os.mkdir("Data/backup")
        except:
            pass
        try:
            while True:
                serial = self.generateSerial()
                if os.path.isfile("Data/backup/Members_" + time.strftime("%Y%m%d-%H%M%S") + "_" + serial + ".csv") == False:
                    break
            shutil.copy("Data/Members.csv", "Data/backup/Members_" +
                        time.strftime("%Y%m%d-%H%M%S") + "_" + serial + ".csv")
            shutil.copy("Data/Books.json", "Data/backup/Books_" +
                        time.strftime("%Y%m%d-%H%M%S") + "_" + serial + ".json")
            shutil.copy("Data/BookItems.json", "Data/backup/BookItems_" +
                        time.strftime("%Y%m%d-%H%M%S") + "_" + serial + ".json")
            return "Backup created"

        except:
            return "Error creating backup"

    def restoreBackUp(self, query):
        try:
            shutil.copy("Data/backup/Members_" + query +
                        ".csv", "Data/Members.csv")
            shutil.copy("Data/backup/Books_" + query +
                        ".json", "Data/Books.json")
            shutil.copy("Data/backup/BookItems_" + query +
                        ".json", "Data/BookItems.json")
            self.loadUsers()
            self.loadBooks()
            self.loadBookItems()
            return "Backup restored"
        except:
            return "Error restoring backup"

    def getBackups(self):
        files = []
        for file in os.listdir("Data/backup"):
            if file.endswith(".csv") or file.endswith(".json"):
                files.append(file)
        for i in range(len(files)):
            files[i] = files[i].split("_")
            files[i] = files[i][1] + "_" + files[i][2]
            files[i] = files[i].split(".")
            files[i] = files[i][0]
        files = [*set(files)]
        return files

    def removeBackUp(self, query):
        try:
            os.remove("Data/backup/Members_" + query + ".csv")
            os.remove("Data/backup/Books_" + query + ".json")
            os.remove("Data/backup/BookItems_" + query + ".json")
            return "Backup removed"
        except:
            return "Error removing backup"
