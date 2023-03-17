import Screens.screen as Screens
import Screens.userScreen as userScreen
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
        username = input()
        print("Please enter your password: ")
        password = input()

        user = login.Login(username, password)
        if user == False:
            super().showError("Invalid username or password")
            self.show()
        else:
            print ("Welcome " + user.username + "!")
            screen = userScreen.UserScreen(user)  
            screen.show()


    