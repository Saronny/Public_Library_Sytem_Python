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
            scr = screen.Screen("Admin Menu", ["Catalog", "Book Menu", "Members Menu", "System Menu", "Logout"])
            scr.setBack("Main Menu")
            choice = scr.show()
        
        elif (choice == "Book Menu"):
            scr = screen.Screen("Book Menu", ["Add book",  "Edit book", "Remove book", "Lend book", "Return book", "See loans", "Back"])
            scr.setBack("Admin Menu")
            choice = scr.show()
            
        elif (choice == "Members Menu"):
            scr = screen.Screen("Members Menu", ["See members", "Register", "Edit member", "Remove member", "Back"])
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
            scr.setBack("Book Menu")
            choice = scr.show()

        elif(choice == "Lend book"):
            if user.getRole() == "User":
                userNumber = user.getNumber()
            else :
                userNumber = 0
            scr = screen.LendBookScreen("Lend book", ["Back"], user.getRole(), userNumber)
            if user.getRole() == "Admin":
                scr.setBack("Book Menu")
            else:
                scr.setBack("User Menu")
            choice = scr.show()

        elif(choice == "Return book"):
            if user.getRole() == "User":
                userNumber = user.getNumber()
            else :
                userNumber = 0 
            scr = screen.ReturnBookScreen("Return book", ["Back"], user.getRole(), userNumber)
            if user.getRole() == "Admin":
                scr.setBack("Book Menu")
            else:
                scr.setBack("User Menu")
            choice = scr.show()
        
        elif(choice == "Remove book"):
            scr = screen.RemoveBookScreen("Remove book", ["Back"])
            scr.setBack("Book Menu")
            choice = scr.show()

        elif(choice == "Register"):
            scr = screen.RegisterScreen("Register", ["Back"])
            scr.setBack("Member Menu")
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
            scr.setBack("Book Menu")
            choice = scr.show()
            
        elif(choice == "Edit member"):
            #TODO: Add edit member screen
            scr = screen.Screen("Edit member", ["Back"])
            scr.setBack("Members Menu")
            choice = scr.show()

            
        elif(choice == "Remove member"):
            scr = screen.RemoveMemberScreen("Remove member", ["Back"])
            scr.setBack("Members Menu")
            choice = scr.show()
            
        elif(choice == "See members"):
            scr = screen.ShowMembersScreen("See members", ["Back"])
            scr.setBack("Members Menu")
            choice = scr.show() 
            
        elif(choice == "System Menu"):
            scr = screen.Screen("System Menu", ["Make back-up", "Restore back-up", "Back"])
            scr.setBack("Admin Menu")
            choice = scr.show()
            
        elif(choice == "Make back-up"):
            #TODO: Add make back-up screen
            scr = screen.Screen("Make back-up", ["Back"])
            scr.setBack("System Menu")
            choice = scr.show()
            
        elif(choice == "Restore back-up"):
            #TODO: add restore back-up screen
            scr = screen.Screen("Restore back-up", ["Back"])
            scr.setBack("System Menu")
            choice = scr.show()

        elif(choice == "See loans"):
            scr = screen.ShowLendBookItems("loanes", ["Back"])
            scr.setBack("Book Menu")
            choice = scr.show()


            
        elif(choice == "Exit"):
            break

        
        

    # if(choice == "Login"):
    #     scr = screen.Screen("Login", ["Back", "Exit"])
    #     scr.show()
    #     choice = scr.get_input()



main()
