'''
Suppose you want to create a program that keeps contact information, such as names, phone numbers, and email addresses. 
You could start by writing a class such as the  class, shown in Program 10-18. An instance of the  class keeps the following data:
                
    * A person’s name is stored in the  attribute.
    * A person’s phone number is stored in the  attribute.
    * A person’s email address is stored in the  attribute.
'''

class Contact():
    def __init__(self, name, phone_num, email):
        self.name = name
        self.phone_num = phone_num
        self.email = email
        
    # Setters
    def set_name(self, name):
        self.name = name
    
    def set_phone_num(self, phone_num):
        self.phone_num = phone_num
        
    def set_email(self, email):
        self.email = email
    
    # Getters
    def get_name(self):
        return self.name
    
    def get_phone_num(self):
        return self.phone_num
    
    def get_email(self):
        return self.email
    
    # __str__ method to return the object as a string
    def __str__(self):
        contact = f"Name: {self.name}\nPhone: {self.phone_num}\nEmail: {self.email}"
        return contact
        