import Screens.screen as sc
import login



class loginScreen(sc.Screen):    

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

        self.login = login.login(self.username, self.password)
        if self.login.login() == False:
            super().showError("Invalid username or password")
            self.show()
        else:
            print ("Welcome " + self.login.login().get_name())


    