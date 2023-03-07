import Screens.screen as Screen
import Screens.loginScreen as loginScreen
import sys

class MainScreen(Screen.Screen):    

    title = "Main Screen"
    menu = ["login", "Exit"]
    screens = [loginScreen.loginScreen()]

    def __init__(self):
        super().__init__(None , self.title, self.menu, self.screens)
    
    def show(self):
        super().show()
    
    def get_input(self):
        return super().get_input()


    


    


    

    