import csv
import persons
import os


class Login:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user = None

    def Login(self):
        if self.username == "admin" and self.password == "admin123":
            self.user = persons.Admin()
            return self.user
        else:
            with open('Data\Members.csv', 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar="'")
                for row in reader:
                    if self.username == row[7] and self.password == row[8]:
                        self.user = persons.User(
                            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[9])
                        return self.user
                    else:
                        self.user = None
