'''
'''

class Robot():
    def __init__(self, name = "", color = "", weight = 0):
        self.name = name
        self.color = color
        self.weight = weight
        
    # Setter
    def set_name(self, name):
        self.name = name
    def set_color(self, color):
        self.color = color
    def set_weight(self, weight):
        self.weight = weight
    
    # Getter
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
    def get_weight(self):
        return self.weight
    
    def introduceSelf(self):
        print(f"Hello, padawn! My name is {self.name} and my favorite color is {self.color}. I am {self.weight} pounds!")
        
class Person():
    def __init__(self, name = "", personality = "", isSitting = bool, robot_owned = ""):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        self.robot_owned = robot_owned
    
    # Setters
    def set_name(self, name):
        self.name = name
    def set_personality(self, personality):
        self.personality = personality
    def set_isSitting(self, isSitting):
        self.isSitting = isSitting

    # Getter
    def get_name(self):
        return self.name
    def get_personality(self):
        return self.personality
    def get_isSitting(self):
        return self.isSitting
   
    def sit_down(self):
        self.isSitting = True
    
    def stand_up(self):
        self.isSitting = False
    
r1 = Robot("Tom", "red", 30)
r1.introduceSelf()
r2 = Robot("Jerry", "blue", 40)
r2.introduceSelf()
r3 = Robot()
r3.set_name("Ollie")
r3.set_color("Gray")
r3.set_weight(55)
r3.introduceSelf()

p1 = Person("Alice", "aggressive", False, r2)
p2 = Person("Becky", "talkative", True, r1)
