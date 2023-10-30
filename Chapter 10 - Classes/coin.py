'''
Intro to classes
'''
import random

class Coin:
    # Simple class for simulating coin toss
    def __init__(self):
        self.__sideup = "Heads"
    def __del__(self):
        pass # Null statement
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
            
    def get_sideup(self):
        return self.__sideup
    
    def __str__(self):
        return "Coin face = " + self.__sideup