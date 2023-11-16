'''
'''
from abc import ABC, abstractmethod

class Automobile(ABC):
    
    def __init__(self, make, model, mileage, price):
        '''
        The __init__ method accepts arguments for the make,
        model, mileage, and price. It initializes the data attributes
        with these values.
        '''

        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        
    
    # Use property decorators
    # for class attributes
    @property
    def make(self):
        return self.__make
    @make.setter
    def make(self, make):
        self.__make = make
        
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        self.__model = model
        
    @property
    def mileage(self):
        return self.__mileage
    @mileage.setter
    def mileage(self, mileage):
        self.__mileage = mileage
        
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
        
    def __str__(self):
        ''' Create a string representation'''
        display_string = str('{} {} with {} miles at ${:,.2f}\n'.format(self.__make,
                                                                            self.__model,
                                                                            self.__mileage,
                                                                            self.__price))
        
        return display_string
    
    @abstractmethod
    def is_off_road(self):
        '''
        abastract method to determine off road capability
        must be override in subclass to instantiate object.
        '''
        pass
    
class Car(Automobile):
    '''
    The car class represents a car. It is a subclass
    of the Automobile class.
    '''
    def __init__(self, make, model, mileage, price, doors):
        '''
        The __init__ method accepts arguments for the
        car's make, model, mileage, price, and doors.
        '''
        
        # Call the superclass __init__ method and pass the required arguments.
        # Note that we also have o pass self as an argument
        Automobile.__init__(self, make, model, mileage, price)
        
        #Initialize the doors atribute
        self.__doors = doors
        
    # Use property decorators
    @property
    def doors(self):
        return self.__doors
    @doors.setter
    def doors(self, doors):
        self.__doors = doors
        
    def __str__(self):
        ''' Create string representation '''
        display_string = Automobile.__str__(self) + \
            str('\twith {} doors'.format(self.__doors))
            
        return display_string
    
    def is_off_road(self):
        '''
        Override parent class abstract method to determine
        off road capability and enable instantiation'''
        return False
    
class Truck(Automobile):
    '''
    The Truck class represents a truck. It is a subclass
    of the Automobile class.
    '''
    def __init__(self, make, model, mileage, price, drive_type):
    
        # Call the superclass __init__ method and pass the required arguments.
        # Note that we also have o pass self as an argument
        Automobile.__init__(self, make, model, mileage, price)
        
        # Initialize the drive_type attribute
        self.__drive_type = drive_type
        
    @property
    def drive_type(self):
        return self.__drive_type
    @drive_type.setter
    def drive_type(self, drive_type):
        self.__drive_type = drive_type
        
    def __str__(self):
        ''' Create a string representation '''
        display_string = Automobile.__str__(self) + \
            str("\twith drive type {}".format(self.__drive_type))
            
        return display_string
    
    def is_off_road(self):
        
        if self.__drive_type == "4WD":
            return True
        else:
            return False    
    
class SUV(Automobile):
        '''
        The SUV class represents a sport utility vehicle. 
        It is a subclass of the Automobile class.
        '''
        
        def __init__(self, make, model, mileage, price, pass_cap):
            '''
            The __init__ method accepts arguments for the
            SUV's make, model, mileage, price, and passenger capacity
            '''
            # Call the superclass __init__ method and pass the required arguments.
            # Note that we also have o pass self as an argument
            Automobile.__init__(self, make, model, mileage, price)
            
            # Initialize the pass_cap
            self.__pass_cap = pass_cap
            
        @property
        def pass_cap(self):
            return self.__pass_cap
        @pass_cap.setter
        def pass_cap(self, pass_cap):
            self.__pass_cap = pass_cap
            
        def __str__(self):
            ''' Create a string representation '''
            display_string = Automobile.__str__(self) + \
                str("\twith {} passenger capacity".format(self.__pass_cap))
                
            return display_string
        
        def is_off_road(self):
            
            if self.__pass_cap <= 2:
                return True
            else:
                return False