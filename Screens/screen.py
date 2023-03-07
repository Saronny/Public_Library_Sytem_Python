import sys
import os


class Screen:

    def __init__(self, previous, title, menu, screens):
        self.previous = previous
        self.title = title
        self.menu = menu
        self.screens = screens

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
            if self.menu[choice] == "Exit":
                self.Exit()
            elif self.menu[choice] == "Back":
                self.Back()
            else:
                self.screens[choice].show()
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

        

    
