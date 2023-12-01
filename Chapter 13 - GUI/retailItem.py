
class RetailItem():
    ''' Class to hold details of retaul item '''
    def __init__(self, description = "", units = 0, price = 0.0):
        '''
        Constructor that receivers description, units and price as an argument.
            Description is a string type
            Units is an integer type
            Price is a float number type
        '''
        self.__description = description
        self.__units = units
        self.__price = price
    
    #  Properties for each attribute to set setters and getters
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self,description):
        self.__description = description
        
    @property
    def units(self):
        return self.__units
    @units.setter
    def units(self,units):
        self.__units = units
        
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
        
    def __str__(self):
        '''
        Method to display the description, units and price of a product.
        '''
        display_string = 'Description: {:20}\nUnits: {:}\nPrice: ${:,.2f}\n'.format(self.__description, self.__units, self.__price)
        return display_string