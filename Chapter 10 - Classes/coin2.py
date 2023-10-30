'''
'''

class Coin:
    #" Simple class for simulting coin toss."
    
    num_coins = 0 # Class level variable
    
    def __init__(self):
        self.__sideup = "Heads"
        Coin.num_coins += 1
        
    def __del__(self):
        type(self).num_coins -= 1
    
    @classmethod
    def show_count(cls):
        print("Total coins:", cls.num_coins)
        
    @staticmethod
    def purpose():
        print("This class simulates a coin toss.")