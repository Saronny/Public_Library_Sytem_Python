import screen

def main(): 
    choice = 0 
    if(choice == 0):
        scr = screen.Screen("Main Menu", ["Login", "Exit"])
        scr.show()


if __name__ == "__main__":
    main()
