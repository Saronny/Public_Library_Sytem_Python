import screen

def main(): 
    
    choice = "Main Menu"
    while(True):
        if(choice == "Main Menu"):
            scr = screen.Screen("Main Menu", ["Login", "Exit"])
            choice = scr.show()
        elif(choice == "Login"):
            scr = screen.Screen("Login", ["Back", "Exit"])
            choice = scr.show()
        elif(choice == "Exit"):
            break

        
        

    # if(choice == "Login"):
    #     scr = screen.Screen("Login", ["Back", "Exit"])
    #     scr.show()
    #     choice = scr.get_input()



main()
