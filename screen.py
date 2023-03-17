import sys
import os


class Screen:

    def __init__(self, title, menu):
      
        self.title = title
        self.menu = menu

    def show(self):
        print(self.title)
        number = 1
        for item in self.menu:
            print(str(number) + ". " + item)
            number += 1
        self.get_input()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def showError(self, error):
        self.clear()
        print(error)

    def get_input(self):
        try:
            choice = int(input())

            if self.menu[choice-1] == "Exit":
                self.Exit()
            elif self.menu[choice-1] == "Back":
                self.Back()
            else:
                return choice
        except ValueError:
            self.showError("Invalid input")
            self.show()
        except IndexError:
            self.showError("Invalid input")
            self.show()

    def Back(self):
        self.previous.show()
    
    def Exit(self):
        sys.exit()

        

    
