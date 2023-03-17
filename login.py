import csv
import persons
import os
class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def Login(self):
        if self.username == "admin" and self.password == "admin123":
            return persons.Admin()
        else:
            with open( "Analysis-3-herkansing\Data\Members.csv", "r") as file:
                reader = csv.reader(file, delimiter=";")
                for row in reader:
                    if self.username == row[7] and self.password == row[8]:
                        return persons.User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[9])
                    else:
                        return False
