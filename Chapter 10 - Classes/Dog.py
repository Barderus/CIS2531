'''
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
        
    def add_one(self, x):
        return x + 1
    def bark(self):
        print("bark")


dog1 = Dog("Tim", 4)
print(dog1.get_name())
print(dog1.get_age())