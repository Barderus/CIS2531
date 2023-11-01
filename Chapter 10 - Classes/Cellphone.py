'''
Wireless Solutions, Inc. is a business that sells cell phones and wireless service. You are a programmer in the company’s IT department, 
and your team is designing a program to manage all of the cell phones that are in inventory. 
You have been asked to design a class that represents a cell phone. The data that should be kept as attributes in the class are as follows:
             Attributes:   
    ** The name of the phone’s manufacturer will be assigned to the  attribute.
    ** The phone’s model number will be assigned to the  attribute.
    ** The phone’s retail price will be assigned to the  attribute.
    
            Methods:
    ** An  method that accepts arguments for the manufacturer, model number, and retail price.
    ** A  method that accepts an argument for the manufacturer. This method will allow us to change the value of the attribute 
        after the object has been created, if necessary.
    ** A  method that accepts an argument for the model. 
        This method will allow us to change the value of the  attribute after the object has been created, if necessary.
    ** A  method that accepts an argument for the retail price. 
        This method will allow us to change the value of the  attribute after the object has been created, if necessary.
    ** A  method that returns the phone’s manufacturer.
    ** A  method that returns the phone’s model number.
    ** A  method that returns the phone’s retail price.
'''

class Cellphone():
    # Dunder method that initializes the attributes of this class
    def __init__(self, manufacturer, model_num, retail_price):
        self.__manufacturer = manufacturer
        self.__model_num = model_num
        self.__retail_price = retail_price
    
    # Setts methods that allow changes in the attributes 
    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer
        
    def set_model_num(self, model_num):
        self.__model_num = model_num
        
    def set_retail_price(self, retail_price):
        self.__retail_price = retail_price
    
    # Get methods to return the attributes
    def get_manufacturer(self):
        return self.__manufacturer
    
    def get_model_num(self):
        return self.__model_num
    
    def get_retail_price(self):
        return self.__retail_price
        
        