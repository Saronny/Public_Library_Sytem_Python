import screen

def main(): 
    
    choice = "Main Menu"
    user = None
    while(True):
        if(choice == "Main Menu"):
            scr = screen.Screen("Main Menu", ["Login", "Exit"])
            choice = scr.show()
        elif(choice == "Login"):
            scr = screen.LoginScreen("Login")
            user = scr.show()
            if user != None:
                if user.getRole() == "Admin":
                    scr = screen.Screen("Admin Menu", ["Logout"])
                    scr.setBack("Main Menu")
                    choice = scr.show()
                else:
                    scr = screen.Screen("User Menu", ["Logout"])
                    scr.setBack("Main Menu")
                    choice = scr.show()
            
        elif(choice == "Exit"):
            break

        
        

    # if(choice == "Login"):
    #     scr = screen.Screen("Login", ["Back", "Exit"])
    #     scr.show()
    #     choice = scr.get_input()



main()
