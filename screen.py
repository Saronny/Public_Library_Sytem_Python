import sys
import os


class Screen:

    def __init__(self, title, menu):
        self.title = title
        self.menu = menu 
        self.Back = ""

    def show(self):
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
            # self.show() 
            choice = int(input())
            if(choice > 0 and choice <= len(self.menu)):
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

   

        

    
