import sys
import Screens.screen as screen
import Screens.mainScreen as mainScreen

def main(): 
    screen = mainScreen.MainScreen()
    screen.clear()
    screen.show()

if __name__ == "__main__":
    main()
