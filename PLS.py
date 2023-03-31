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
            scr = screen.Screen("Admin Menu", ["Catalog", "Books", "Members", "System", "Logout"])
            scr.setBack("Main Menu")
            choice = scr.show()
        
        elif (choice == "Books"):
            scr = screen.Screen("Books", ["Add book",  "Edit book", "Remove book", "Lend book", "Return book", "Back"])
            scr.setBack("Admin Menu")
            choice = scr.show()
            
        elif (choice == "Members"):
            scr = screen.Screen("Members", ["See members", "Register", "Edit member", "Remove member", "Back"])
            scr.setBack("Admin Menu")
            choice = scr.show()
            
            
        elif (choice == "User Menu"):
            scr = screen.Screen("User Menu", ["Catalog", "Lend book", "Return book", "Logout"])
            scr.setBack("Main Menu")
            choice = scr.show()

        elif(choice == "Search Catalog"):
            scr = screen.SearchScreen("Search Catalog", ["Back"])
            scr.setBack("Catalog")
            choice = scr.show()

        elif(choice == "Add book"):
            scr = screen.AddBookScreen("Add book", ["Back"])
            scr.setBack("Books")
            choice = scr.show()

        elif(choice == "Lend book"):
            #TODO: Add lend book screen
            scr = screen.Screen("Lend book", ["Back"])
            if user.getRole() == "Admin":
                scr.setBack("Books")
            else:
                scr.setBack("User Menu")
            choice = scr.show()

        elif(choice == "Return book"):
            #TODO: Add return book screen
            scr = screen.Screen("Return book", ["Back"])
            if user.getRole() == "Admin":
                scr.setBack("Books")
            else:
                scr.setBack("User Menu")
            choice = scr.show()
        
        elif(choice == "Remove book"):
            scr = screen.RemoveBookScreen("Remove book", ["Back"])
            scr.setBack("Books")
            choice = scr.show()

        elif(choice == "Register"):
            scr = screen.RegisterScreen("Register", ["Back"])
            scr.setBack("Members")
            choice = scr.show()
            
        elif (choice == "Catalog"):
            scr = screen.Screen("Catalog", ["Show Catalog", "Search Catalog", "Back"])
            if user.getRole() == "Admin":
                scr.setBack("Admin Menu")
            else:
                scr.setBack("User Menu")
            choice = scr.show()
            
        elif(choice == "Show Catalog"):
            scr = screen.ShowCatalogScreen("Show Catalog", ["Back"])
            scr.setBack("Catalog")
            choice = scr.show()
            
        elif(choice == "Edit book"):
            #TODO: Add edit book screen
            scr = screen.Screen("Edit book", ["Back"])
            scr.setBack("Books")
            choice = scr.show()
            
        elif(choice == "Edit member"):
            #TODO: Add edit member screen
            scr = screen.Screen("Edit member", ["Back"])
            scr.setBack("Members")
            choice = scr.show()
            
        elif(choice == "Remove member"):
            #TODO: Add remove member screen
            scr = screen.Screen("Remove member", ["Back"])
            scr.setBack("Members")
            choice = scr.show()
            
        elif(choice == "See members"):
            #TODO: Add see members screen
            scr = screen.Screen("See members", ["Back"])
            scr.setBack("Members")
            choice = scr.show() 
            
        elif(choice == "Exit"):
            break

        
        

    # if(choice == "Login"):
    #     scr = screen.Screen("Login", ["Back", "Exit"])
    #     scr.show()
    #     choice = scr.get_input()



main()
