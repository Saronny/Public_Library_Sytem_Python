import system as system
import os
import login as login
import time


class Screen:
    
    sys = system.System()

    def __init__(self, title, menu):
        self.title = title
        self.menu = menu 
        self.Back = ""
        

    def show(self):
        self.clear()
        print("=== " + self.title  + " ===")
        number = 1
        for item in self.menu:
            print("[" + str(number) + "] " + item)
            number += 1
        return self.get_input()
        

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def showMessage(self, error):
        self.clear()
        print(error)
        time.sleep(1)
        

    def get_input(self):
        try:
            print("=====================================")
            choice = int(input("Enter your choice: "))
            if(choice > 0 and choice <= len(self.menu)):
                if self.menu[choice-1] == "Back" or self.menu[choice-1] == "Logout":
                    return self.Back
                return self.menu[choice-1]
            else:
                self.showMessage("Invalid input")
                return self.show()
        except ValueError:
            self.showMessage("Invalid input")
            return self.show()
        except IndexError:
            self.showMessage("Invalid input")
            return self.show()

    def setBack(self, back):
        self.Back = back

class LoginScreen(Screen):
    def __init__(self, title):
        self.title = title
        self.username = ""
        self.password = "" 

    def show(self):
        self.clear()
        print("=== " + self.title  + " ===")
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        self.login = login.Login(self.username, self.password)
        self.login.Login()
        if self.login.user != None:
            return self.login.user
        else:
            self.showMessage("Invalid username or password")
            return None


class SearchScreen(Screen):
    def __init__(self, title, menu):
        self.title = title
        self.menu = menu 
        self.Back = ""
        # self.sys = system.System()
        
        
        
    def show(self):
        self.clear()
        print ("=== " + self.title + " ===")
        self.request = input("Enter your search request: ")
        self.search = self.sys.search(self.request)
        
        if self.search != "No results found":
            for item in self.search:
                print("[*] " + item.getAuthor() + " - " + item.getTitle() +  " ---------------- Availibility: " + str(self.sys.getBookAvailable(item.getTitle())))
            number = 1
            print("=====================================")
            for item in self.menu:
                print("[" + str(number) + "] " + item)
                number += 1
            return self.get_input()
        else :
            self.showMessage("No results found")
            return self.Back
        
    # def setBack(self, back):
    #     self.Back = back

class AddBookScreen(Screen):
    def __init__(self, title, menu):
        self.title = title
        self.menu = menu 
        self.Back = ""
        # self.sys = system.System()
        
    def show(self):
        self.clear()
        print ("=== " + self.title + " ===")
        self.author = input("Enter the author: ")
        self.country = input("Enter the country: ")
        self.imageLink = input("Enter the image link: ")
        self.link = input("Enter the link: ")
        try:
            self.pages = int(input("Enter the number of pages: "))
        except ValueError:
            self.showMessage("Number of pages must be a number")
            return self.Back
        self.title = input("Enter the title: ")
        self.ISBN = input("Enter the ISBN: ")
        try:
            self.year = int(input("Enter the year: "))
        except ValueError:
            self.showMessage("Year must be a number")
            return self.Back
        self.book = self.sys.AddBook(self.author, self.country, self.imageLink, self.link, self.pages, self.title, self.ISBN, self.year)
        if self.book != "Book added":
            self.showMessage("Book not added - ISBN already exists")
            return self.Back
        else:
            self.showMessage("Book added")
            return self.Back
        
class RegisterScreen (Screen):
    def __init__(self, title, menu):
        self.title = title
        self.menu = menu 
        self.Back = ""
        # self.sys = system.System()
        
    def show(self):
        self.clear()
        print ("=== " + self.title + " ===")
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        self.name = input("Enter name: ")
        self.surname = input("Enter surname: ")
        self.email = input("Enter email: ")
        self.phone = input("Enter phone number: ")
        self.address = input("Enter address: ")
        self.zipcode = input("Enter zipcode: ")
        self.city = input("Enter city: ")
        self.register = self.sys.register(self.name, self.surname, self.address, self.zipcode, self.city, self.email, self.username, self.password, self.phone)
        self.showMessage(self.register)
        return self.Back
    
class RemoveBookScreen (Screen):
    def __init__(self, title, menu):
        self.title = title
        self.menu = menu 
        self.Back = ""
        # self.sys = system.System()
        
    def show(self):
        self.clear()
        print ("=== " + self.title + " ===")
        self.ISBN = input("Enter the ISBN of the book you want to remove: ")
        self.remove = self.sys.removeBook(self.ISBN)
        self.showMessage(self.remove)
        return self.Back
    
    
class ShowCatalogScreen(Screen):
    def __init__(self, title, menu):
        self.title = title
        self.menu = menu 
        self.Back = ""
        # self.sys = system.System()
        self.books = self.sys.getBooks()
        
    def show(self):
        self.clear()
        print ("=== " + self.title + " ===")
        for item in self.books:
            print("[*] " + item.getTitle() + " ---------------- Availibility: " + str(self.sys.getBookAvailable(item.getTitle())))
        number = 1
        print("=====================================")
        for item in self.menu:
            print("[" + str(number) + "] " + item)
            number += 1
        return self.get_input()
    

class ShowMembersScreen(Screen):
    def __init__(self, title, menu):
        self.title = title
        self.menu = menu 
        self.Back = ""
        self.members = self.sys.getMembers()
        
    def show(self):
        self.clear()
        print ("=== " + self.title + " ===")
        if self.members != "No members found":
            for item in self.members:
                print("[*] " + item.getNumber() + ". " + item.getUsername() + " ---------------- " + item.getEmail())
            number = 1
            print("=====================================")
            for item in self.menu:
                print("[" + str(number) + "] " + item)
                number += 1
        else:
            print(self.members)
        return self.get_input()
    
class LendBookScreen(Screen):
    def __init__(self, title, menu, role, userNumber=0):
        self.title = title
        self.menu = menu 
        self.Back = ""
        self.role = role
        self.userNumber = userNumber
    
    def show(self):
        self.clear()
        print ("=== " + self.title + " ===")
        if self.role == "User":
            query = input("Enter the ISBN or Title of the book you want to lend: ")
            self.lend = self.sys.lendBook(query, self.userNumber)
            if self.lend == "Member has already lent 3 books":
                self.showMessage("You have already lent 3 books")
                return self.Back
            if self.lend == "Member has already lent this book":
                self.showMessage("You have already lent this book")
                return self.Back
            self.showMessage(self.lend)
            return self.Back
        else:
            self.userNumber = input("Enter the number or username of the member you want to lend the book to: ")
            query = input("Enter the ISBN or Title of the book you want to lend: ")
            self.lend = self.sys.lendBook(query, self.userNumber)
            self.showMessage(self.lend)
            return self.Back 
        
class ReturnBookScreen(Screen):
    def __init__(self, title, menu, role, userNumber=0):
        self.title = title
        self.menu = menu
        self.Back = ""
        self.role = role
        self.userNumber = userNumber
        if self.role == "User":
            self.lentBooks = self.sys.getLoanedBooks(self.userNumber)
        else:
            self.lentBooks = []
            
    
    def show(self):
        self.clear()
        print ("=== " + self.title + " ===")
        if self.role == "User":
            if self.lentBooks == []:
                self.showMessage("You have no books to return")
                return self.Back
            num = 1
            for item in self.lentBooks:
                print("[" + str(num) + "] " + item.getTitle() + " " + item.getISBN() + " ---------------- Due date: " + item.getDate())
                num += 1
            print ("=====================================")
            print ("[0] Back")
            try:
                query = int(input("Enter a number: "))
                if query == 0:
                    return self.Back
                self.returnBook = self.sys.returnBook(self.lentBooks[query-1].getTitle(), self.userNumber)
                self.showMessage(self.returnBook)
                return self.Back
            except:
                self.showMessage("Invalid input")
                return self.Back
            
           
        else:
            self.userNumber = input("Enter the number or username of the member you want to return the book from: ")
            self.lentBooks = self.sys.getLoanedBooks(self.userNumber)
            if self.lentBooks == []:
                self.showMessage("Member has no books to return")
                return self.Back
            num = 1
            for item in self.lentBooks:
                print("[" + str(num) + "] " + item.getTitle() + " " + item.getISBN() + " ---------------- Due date: " + item.getDate())
                num += 1
            print ("=====================================")
            print ("[0] Back")
            try:
                query = int(input("Enter a number: "))
                if query == 0:
                    return self.Back
                self.returnBook = self.sys.returnBook(self.lentBooks[query-1].getTitle(), self.userNumber)
                self.showMessage(self.returnBook)
                return self.Back
            except:
                self.showMessage("Invalid input")
                return self.Back

class ShowLendBookItems(Screen): 
    def __init__(self, title, menu):
        self.title = title
        self.menu = menu
        self.Back = ""
        self.loans = self.sys.getAllLoanedBooks()
            
    
    def show(self):
        self.clear() 
        print ("=== " + self.title + " ===")
        if self.loans == []:
            self.showMessage("There are no books lent")
            return self.Back
        for item in self.loans:
            print("[*] " + self.sys.getMemberUsername(item.getUserNumber()) + ": " + item.getTitle() +  " - " + item.getISBN() + " ---------------- Due date: " + item.getDate())
        number = 1
        print("=====================================")
        for item in self.menu:
            print("[" + str(number) + "] " + item)
            number += 1
        return self.get_input()

        

class RemoveBookScreen(Screen):
    def __init__(self, title, menu):
        self.title = title
        self.menu = menu
        self.Back = ""
        self.books = self.sys.getBooks()
        
    def show(self):
        self.clear()
        print ("=== " + self.title + " ===")
        if self.books == []:
            self.showMessage("There are no books to remove")
            return self.Back
        num = 1
        for item in self.books:
            print("[" + str(num) + "] " + item.getTitle() + " " + item.getISBN())
            num += 1
        print ("=====================================")
        print ("[0] Back")
        try:
            query = int(input("Enter a number: "))
            if query == 0:
                return self.Back
            self.remove = self.sys.removeBook(self.books[query-1].getTitle())
            self.showMessage(self.remove)
            return self.Back
        except:
            self.showMessage("Invalid input")
            return self.Back
    
class RemoveMemberScreen(Screen):
    def __init__(self, title, menu):
        self.title = title
        self.menu = menu
        self.Back = ""
        self.members = self.sys.getMembers()
        
    def show(self):
        self.clear()
        print ("=== " + self.title + " ===")
        if self.members == []:
            self.showMessage("There are no members to remove")
            return self.Back
        num = 1
        for item in self.members:
            print("[" + str(num) + "] " + item.getUsername() + " " + item.getNumber())
            num += 1
        print ("=====================================")
        print ("[0] Back")
        try:
            query = int(input("Enter a number: "))
            if query == 0:
                return self.Back
            self.remove = self.sys.removeMember(self.members[query-1].getNumber())
            self.showMessage(self.remove)
            return self.Back
        except:
            self.showMessage("Invalid input")
            return self.Back
    