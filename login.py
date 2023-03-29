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
            try: 
                with open('Data/Members.csv', 'r') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',')
                    for row in reader:
                        if row[0] == self.username and row[1] == self.password:
                            self.user = persons.User(row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                            return self.user
            except:
                print("Error loading users")
                return None
