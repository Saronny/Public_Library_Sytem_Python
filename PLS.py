import screen

# TODO: Add a screen for the user to see the books he has lent (this can be seen in the return books screen)
# TODO: test user input in all screens (tested)
# TODO: Test if files get created if they don't exist Members.csv and books.json
# TODO: Test all edit functions in system.py for users and books NOTE: if books are edited, the bookitems are also edited!
# TODO: Test all remove functions in system.py for users and books NOTE: if books are removed, the bookitems are also removed!
# TODO: Test all lend and return functions in system.py for users and admin
# TODO: Test all search functions in system.py for books
# TODO: Test backup and restore functions in system.py for admin (there was an error if you try to restore a backup if there are no backups => fixed)
# TODO: Test register user function in system.py for admin
# TODO: Test add book function in system.py for admin #NOTE if a book is added, the 5 bookitems are also added!


def main():

    choice = "Main Menu"
    user = None
    while (True):
        if (choice == "Main Menu"):
            user = None
            scr = screen.Screen("Main Menu", ["Login", "Exit"])
            choice = scr.show()
        elif (choice == "Login"):
            scr = screen.LoginScreen("Login")
            user = scr.show()
            if user != None:
                if user.getRole() == "Admin":
                    choice = "Admin Menu"
                else:
                    choice = "User Menu"
            else:
                choice = "Main Menu"

        elif (choice == "Admin Menu"):
            scr = screen.Screen(
                "Admin Menu", ["Catalog", "Book Menu", "Members Menu", "System Menu", "Logout"])
            scr.setBack("Main Menu")
            choice = scr.show()

        elif (choice == "Book Menu"):
            scr = screen.Screen("Book Menu", [
                                "Add book",  "Edit book", "Remove book", "Lend book", "Return book", "See loans", "Back"])
            scr.setBack("Admin Menu")
            choice = scr.show()

        elif (choice == "Members Menu"):
            scr = screen.Screen("Members Menu", [
                                "See members", "Register", "Edit member", "Remove member", "Back"])
            scr.setBack("Admin Menu")
            choice = scr.show()

        elif (choice == "User Menu"):
            scr = screen.Screen(
                "User Menu", ["Catalog", "Lend book", "See loans", "Return book", "Logout"])
            scr.setBack("Main Menu")
            choice = scr.show()

        elif (choice == "Search Catalog"):
            scr = screen.SearchScreen("Search Catalog", ["Back"])
            scr.setBack("Catalog")
            choice = scr.show()

        elif (choice == "Add book"):
            scr = screen.AddBookScreen("Add book", ["Back"])
            scr.setBack("Book Menu")
            choice = scr.show()

        elif (choice == "Lend book"):
            if user.getRole() == "User":
                userNumber = user.getNumber()
            else:
                userNumber = 0
            scr = screen.LendBookScreen(
                "Lend book", ["Back"], user.getRole(), userNumber)
            if user.getRole() == "Admin":
                scr.setBack("Book Menu")
            else:
                scr.setBack("User Menu")
            choice = scr.show()

        elif (choice == "Return book"):
            if user.getRole() == "User":
                userNumber = user.getNumber()
            else:
                userNumber = 0
            scr = screen.ReturnBookScreen(
                "Return book", ["Back"], user.getRole(), userNumber)
            if user.getRole() == "Admin":
                scr.setBack("Book Menu")
            else:
                scr.setBack("User Menu")
            choice = scr.show()

        elif (choice == "Remove book"):
            scr = screen.RemoveBookScreen("Remove book", ["Back"])
            scr.setBack("Book Menu")
            choice = scr.show()

        elif (choice == "Register"):
            scr = screen.RegisterScreen("Register", ["Back"])
            scr.setBack("Members Menu")
            choice = scr.show()

        elif (choice == "Catalog"):
            scr = screen.Screen(
                "Catalog", ["View Catalog", "Search Catalog", "Back"])
            if user.getRole() == "Admin":
                scr.setBack("Admin Menu")
            else:
                scr.setBack("User Menu")
            choice = scr.show()

        elif (choice == "View Catalog"):
            scr = screen.ShowCatalogScreen("Catalog", ["Back"])
            scr.setBack("Catalog")
            choice = scr.show()

        elif (choice == "Edit book"):
            scr = screen.EditBookScreen("Edit book", ["Back"])
            scr.setBack("Book Menu")
            choice = scr.show()

        elif (choice == "Edit member"):
            scr = screen.EditMemberScreen("Edit member", ["Back"])
            scr.setBack("Members Menu")
            choice = scr.show()

        elif (choice == "Remove member"):
            scr = screen.RemoveMemberScreen("Remove member", ["Back"])
            scr.setBack("Members Menu")
            choice = scr.show()

        elif (choice == "See members"):
            scr = screen.ShowMembersScreen("See members", ["Back"])
            scr.setBack("Members Menu")
            choice = scr.show()

        elif (choice == "System Menu"):
            scr = screen.Screen(
                "System Menu", ["Make back-up", "Restore back-up", "Remove back-up", "Back"])
            scr.setBack("Admin Menu")
            choice = scr.show()

        elif (choice == "Make back-up"):
            scr = screen.MakeBackupScreen("Make back-up", ["Back"])
            scr.setBack("System Menu")
            choice = scr.show()

        elif (choice == "Restore back-up"):
            scr = screen.RestoreBackupScreen("Restore back-up", ["Back"])
            scr.setBack("System Menu")
            choice = scr.show()

        elif (choice == "See loans"):
            scr = screen.ShowLendBookItems("Loanes", ["Back"])
            scr.setBack("Book Menu")
            choice = scr.show()

        elif (choice == "Remove back-up"):
            scr = screen.DeleteBackupScreen("Remove back-up", ["Back"])
            scr.setBack("System Menu")
            choice = scr.show()

        elif (choice == "Exit"):
            break


main()
