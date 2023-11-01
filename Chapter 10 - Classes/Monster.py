'''
     dunder method is a method that is not called by te user. Instead
     it is called by python when something happens.
     
     Clear code Yt
'''

class Monster():
    
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    
    def __str__(self):
        display_string = (f"A monster with {self.health} and {self.energy} has appeared.")
        return display_string
    
    def update_energy(self, amount):
        self.energy += amount
        
    def get_damage(self, amount):
        self.health -= amount
    
class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster
        
    def attack(self):
        self.monster.get_damage(self.damage)
        
class Attack():
        
    def bite(self):
        print("The monster uses bite!")
    def strike(self):
        print("The monster uses strike")
    def slash(self):
        print("The monster uses slash")
    def kick(self):
        print("The monster uses kick")

monster = Monster(100, 50)
hero = Hero(15, monster)
print(monster.health)
hero.attack()
print(monster.health)