'''
Author: Gabriel dos Reis
Date: 11/13/2023
Program: Employee.py
Description:
Write an  class that keeps data attributes for the following pieces of information:
    * Employee name
    * Employee number
'''
from abc import ABC, abstractmethod

class Employee():
    '''
    Employee class represents an employee and its number
    '''
    hours = 40
    weeks = 52
    
    def __init__(self, name, number):
        '''
        The __init__ method accepts the following arguments:
            name : String
            number : String
        '''
        self.__name = name
        self.__number = number
    
    # Property decorator
    # Getters and Setters for name and number
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number):
        self.__number = number
    
     
    def __str__(self):
        ''' Display class representation in a string '''
        display_string = f"Employee name: {self.__name}\nEmployee number: {self.__number}"
        
        return display_string
    
    @abstractmethod
    def gross_pay(self):
        '''
        abastract method to determine yearly gross pay
        must be override in subclass to instantiate object.
        '''
        pass

'''
Write a class named ProductionWorker that is a subclass of the class Employee. 
The  class should keep data attributes for the following information:
    * Shift number (an integer, such as 1, 2, or 3)
    * Hourly pay rate
The workday is divided into two shifts: 
    * day (1) and night(2) 
Write the appropriate accessor and mutator methods for each class.
Once you have written the classes, write a program that creates an object of the  class and 
prompts the user to enter data for each of the object’s data attributes. 
Store the data in the object, then use the object’s accessor methods to retrieve it and display it on the screen.
'''
class ProductionWorker(Employee):
    '''
        ProductionWorker is a subclass of Employee
    '''
    def __init__(self, name, number, shift_number, pay_rate):
        '''
            The __init__ method accepts two arguments:
                Shift number : Integer
                Hourly pay rate : Float
        '''
        # Call the superclass __init__ method and pass the required arguments.
        Employee.__init__(self, name, number)
        
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate
    
    # Property decorators
    # Setters and getters for shift_number and pay_rate  
    @property
    def shift_number(self):
        return self.__shift_number
    @shift_number.setter
    def shift_number(self, shift_number):
        self.__shift_number = shift_number
        
    @property
    def pay_rate(self):
        return self.__pay_rate
    @pay_rate.setter
    def pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate
        
    def determineShift(self):
        if self.__shift_number == 1:
            return "Day shift (1)"
        elif self.__shift_number == 2:
            return "Night shift (2)"
        else:
            return "Invalid shift value"
        
    def gross_pay(self):
        gross_pay = self.__pay_rate * Employee.hours * Employee.weeks
        return gross_pay
    
    def __str__(self):
        ''' String represetation of the class '''
        display_string = Employee.__str__(self) + \
            f"Shift: {ProductionWorker.determineShift}\nHourly pay rate: {self.__pay_rate}"
        
        return display_string
        
'''

Write a class that is a subclass of the class of the Employee class
The  class should keep a data attribute for the annual salary, 
and a data attribute for the annual production bonus that a shift supervisor has earned. 
'''    
class ShiftSupervisor(Employee):
    
    def __init__(self, name, number, salary, bonus ):
        
        Employee.__init__(self, name, number)
        
        self.__salary = salary
        self.__bonus = bonus
    
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        self.__salary = salary
        
    @property
    def bonus(self):
        return self.__bonus
    @bonus.setter
    def bonus(self, bonus):
        self.__bonus = bonus
        
    def gross_pay(self):
        gross_pay = self.__salary + self.__bonus
        return gross_pay
    
    def __str__(self):
        ''' String representation of the class ShiftSupervisor '''
        display_string = Employee.__str__(self) + \
            f"Annual Salary: {self.__salary}\n Bonus Production: {self.__bonus}"
        return display_string
