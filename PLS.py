import screen
import system
import time

def main(): 
    
    choice = "Main Menu"
    user = None
    while(True):
        if(choice == "Main Menu"): 
            user = None
            scr = screen.Screen("Main Menu", ["Login", "Exit"])
            choice = scr.show()
        elif(choice == "Login"):
            scr = screen.LoginScreen("Login")
            user = scr.show()
            if user != None:
                if user.getRole() == "Admin":
                    choice = "Admin Menu"
                else:
                   choice = "User Menu"
            else:
                choice = "Main Menu"
            

        elif(choice == "Admin Menu"):
            scr = screen.Screen("Admin Menu", ["Search Catalog", "Add book", "Remove book", "Register", "Logout"])
            scr.setBack("Main Menu")
            choice = scr.show()

        elif (choice == "User Menu"):
            scr = screen.Screen("User Menu", ["Search Catalog", "Lend book", "Return book", "Logout"])
            scr.setBack("Main Menu")
            choice = scr.show()

        elif(choice == "Search Catalog"):
            scr = screen.SearchScreen("Search Catalog", ["Back"])
            scr.setBack("User Menu")
            if user.getRole() == "Admin":
                scr.setBack("Admin Menu")
            choice = scr.show()

        elif(choice == "Add book"):
            scr = screen.AddBookScreen("Add book", ["Back"])
            scr.setBack("Admin Menu")
            choice = scr.show()

        elif(choice == "Lend book"):
            scr = screen.Screen("Lend book", ["Back"])
            scr.setBack("User Menu")
            choice = scr.show()

        elif(choice == "Return book"):
            scr = screen.Screen("Return book", ["Back"])
            scr.setBack("User Menu")
            choice = scr.show()
        
        elif(choice == "Remove book"):
            scr = screen.RemoveBookScreen("Remove book", ["Back"])
            scr.setBack("Admin Menu")
            choice = scr.show()

        elif(choice == "Register"):
            scr = screen.RegisterScreen("Register", ["Back"])
            scr.setBack("Admin Menu")
            choice = scr.show()
            
        elif(choice == "Exit"):
            break

        
        

    # if(choice == "Login"):
    #     scr = screen.Screen("Login", ["Back", "Exit"])
    #     scr.show()
    #     choice = scr.get_input()



main()
