'''
Write a class named Procedure that represents a medical procedure that has been performed on a patient. 
The Procedure class should have attributes for the following data:
    •	Name of the procedure 
    •	Date of the procedure 
    •	Name of the practitioner who performed the procedure 
    •	Charges for the procedure 
The Procedure class’s _ _init_ _ method should accept an argument for each attribute. 
The Procedure class should also have accessor and mutator methods for each attribute.

'''
class Procedure():
    def __init__(self, name, date, doc_name, charge = 0.00 ):
        """
        Construcor that has the following attributes:
            * name -> Name : String
            * date-> Date : String
            * doc_name - > Doctor name who did performed the procedure : String
            * changes -> Changes for the procedure : String
        """
        self.__name = name
        self.__date = date
        self.__doc_name = doc_name
        self.__charge = charge
    
    # Setters and getters
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date):
        self.__date = date
        
    @property
    def doc_name(self):
        return self.__doc_name
    @doc_name.setter
    def doc_name(self, doc_name):
        self.__doc_name = doc_name
        
    @property
    def charge(self):
        return self.__charge
    @charge.setter
    def charge(self, charge):
        self.__charge = charge
        
    def __str__(self):
        string = f"Procedure name: {self.__name}\nDate of Procedure: {self.__date}\nDoctor's name: {self.__doc_name}\nCharges: ${int(self.__charge)}"
        
        return string
    