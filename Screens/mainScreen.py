import Screens.screen as Screens
import Screens.loginScreen as loginScreen
import sys

class MainScreen(Screens.Screen):    

    title = "Main Screen"
    menu = ["Login", "Exit"]
    screens = [loginScreen.LoginScreen()]

    def __init__(self):
        super().__init__(None , self.title, self.menu, self.screens)


    


    


    

    