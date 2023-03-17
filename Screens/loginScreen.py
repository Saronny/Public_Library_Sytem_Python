import Screens.screen as Screens
import login



class LoginScreen(Screens.Screen):    

    title = "Login Screen"
    menu = []
    screens = [] 

    def __init__(self):
        super().__init__(None , self.title, self.menu, self.screens)

    def show(self):
        print(self.title)
        print("Please enter your username: ")
        self.username = input()
        print("Please enter your password: ")
        self.password = input()

        self.login = login.Login(self.username, self.password)
        if login.Login == True:
            print ("Welcome " + self.login.Login().get_name())
        else:
            super().showError("Invalid username or password")


    