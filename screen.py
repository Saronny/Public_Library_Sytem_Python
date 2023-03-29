import system as system
import os
import login as login
import time



class Screen:

    def __init__(self, title, menu):
        self.title = title
        self.menu = menu 
        self.Back = ""
        self.sys = system.System()

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
            choice = int(input())
            if(choice > 0 and choice <= len(self.menu)):
                if self.menu[choice-1] == "Back" or self.menu[choice-1] == "Logout":
                    return self.Back
                return self.menu[choice-1]
            else:
                self.showMessage("Invalid input")
                self.get_input()
        except ValueError:
            self.showMessage("Invalid input")
            self.get_input()	
        except IndexError:
            self.showMessage("Invalid input")
            self.get_input()

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
        self.sys = system.System()
        
        
        
    def show(self):
        self.clear()
        print ("=== " + self.title + " ===")
        self.request = input("Enter your search request: ")
        self.search = self.sys.search(self.request)
        
        if self.search != "No results found":
            for item in self.search:
                print("[*] " + item)
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
        self.sys = system.System()
        
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
    
    

   
class AddUserScreen(Screen):
    def __init__(self, title, menu):
        self.title = title
        self.menu = menu 
        self.Back = ""
        self.sys = system.System()
        
    def show(self):
        self.clear()
        print ("=== " + self.title + " ===")
        self.name = input("Enter the name: ")
        self.surname = input("Enter the surname: ")
        self.email = input("Enter the email: ")
        self.phone = input("Enter the phone number: ")
        self.address = input("Enter the address: ")
        self.city = input("Enter the city: ")
        self.country = input("Enter the country: ")
        self.username = input("Enter the username: ")
        self.password = input("Enter the password: ")
        self.user = self.sys.register(self.name, self.surname, self.email, self.phone, self.address, self.city, self.country, self.username, self.password)
        if self.user != "User added":
            self.showMessage(self.user)
            return self.Back
        else:
            self.showMessage(self.user)
            return self.Back
        

    
