import csv
import persons

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def Login(self):
        if self.username == "admin" and self.password == "admin123":
            return persons.Admin()
        else:
            with open("Data/Members.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if self.username == row[7] and self.password == row[8]:
                        return True
                    else:
                        return False
