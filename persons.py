class Person: 
    def __init__(self, name):
        self.name = name
        self.Role = "Person"
    
    def getName(self):
        return self.name
    
    def getRole(self):
        return self.Role

class User(Person):
    def __init__(self, number, name, surname, address, zipcode, city, email, username, telephone):
        super().__init__(name)
        self.number = number
        self.email = email
        self.telephone = telephone
        self.address = address
        self.zipcode = zipcode
        self.city = city
        self.surname = surname
        self.username = username
        self.Role = "User"
        
    def getEmail(self):
        return self.email
    
    def getTelephone(self):
        return self.telephone
    
    def getAddress(self):
        return self.address 
    
    def getNumber(self):
        return self.number
    
    def getZipcode(self):
        return self.zipcode
    
    def getCity(self):
        return self.city
    
    def getSurname(self):
        return self.surname
    
    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password
    
    def getUsername(self):
        return self.username
    
    



class Admin(Person):

    def __init__(self):
        super().__init__("Admin")
        self.Role = "Admin"