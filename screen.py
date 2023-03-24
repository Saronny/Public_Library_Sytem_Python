import sys
import os
import login as login


class Screen:

    def __init__(self, title, menu):
        self.title = title
        self.menu = menu 
        self.Back = ""

    def show(self):
        self.clear()
        print("=== " + self.title  + " ===")
        number = 1
        for item in self.menu:
            print(str(number) + ". " + item)
            number += 1
        return self.get_input()
        

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def showError(self, error):
        self.clear()
        print(error)

    def get_input(self):
        try:
            choice = int(input())
            if(choice > 0 and choice <= len(self.menu)):
                if self.menu[choice-1] == "Back" or self.menu[choice-1] == "Logout":
                    return self.Back
                return self.menu[choice-1]
            else:
                self.showError("Invalid input")
                self.get_input()
        except ValueError:
            self.showError("Invalid input")
            self.get_input()	
        except IndexError:
            self.showError("Invalid input")
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
            self.showError("Invalid login")
            self.show()



    
       


   

        

    
