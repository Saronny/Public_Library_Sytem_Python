class Person: 
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name


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
        
    def get_email(self):
        return self.email
    
    def get_telephone(self):
        return self.telephone
    
    def get_address(self):
        return self.address + " " + self.zipcode + " " + self.city 
    
    def get_number(self):
        return self.number
    
    def full_name(self):
        return self.name + " " + self.surname
    
    def get_username(self):
        return self.username


class Admin(Person):

    def __init__(self):
        super().__init__("Admin")