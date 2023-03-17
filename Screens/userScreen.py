import Screens.screen as Screens



class UserScreen(Screens.Screen):

    title = "User Screen"
    menu = ["Catalog", "Return book", "Loan book", "Logout"]
    screens = ["TODO", "TODO", "TODO"]

    def __init__(self, user):
        super().__init__(title=self.title, menu=self.menu, screens=self.screens)
        self.user = user

    

    
    
        