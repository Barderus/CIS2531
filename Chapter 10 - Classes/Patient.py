'''
Write a class named Patient that has attributes for the following data:
	* First name
    * Middle name
    * Last name 
	* Address
    * City
    * State
    * ZIP code 
	* Phone number 
	* Name and phone number of emergency contact 
The Patient class’s _ _init_ _ method should accept an argument for each attribute. 
The Patient class should also have accessor and mutator methods for each attribute.

'''
class Patient():
    def __init__(self, fname, mname, lname, address, city, state, zip, phone_num, emerg_name, emerg_phone_num):
        """
        Constructor that takes the following attributes
            * fname -> First name : String
            * mname -> Middle name : String
            * lname -> Last name : String
            * address -> Address : String
            * city -> City : String
            * state -> State : String
            * zip -> ZIP code : String
            * phone_num -> Phone number : String
            * emerg_name -> Emergency number : String
            * emerg_phone_num -> Emergency Phone Number : String
        """
        self.__fname = fname
        self.__mname = mname
        self.__lname = lname
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip
        self.__phone_num = phone_num
        self.__emerg_name = emerg_name
        self.__emerg_phone_num = emerg_phone_num
        
    # Setters and getters using decorators
    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self,fname):
        self.__fname = fname
        
    @property
    def mname(self):
        return self.__mname
    @mname.setter
    def mname(self,mname):
        self.__units = mname
        
    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self, lname):
        self.__lname = lname
        
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,address):
        self.__address = address
        
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self,city):
        self.__city = city
        
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state):
        self.__state = state
        
    @property
    def zip(self):
        return self.__zip
    @zip.setter
    def zip(self, zip):
        self.__zip = zip
        
    @property
    def phone_num(self):
        return self.__phone_num
    @phone_num.setter
    def phone_num(self, phone_num):
        self.__phone_num = phone_num
        
    @property
    def emerg_name(self):
        return self.__emerg_name
    @emerg_name.setter
    def emerg_name(self, emerg_name):
        self.__emerg_name = emerg_name
        
    @property
    def emerg_phone_num(self):
        return self.__emerg_phone_num
    @emerg_phone_num.setter
    def emerg_phone_num(self, emerg_phone_num):
        self.__emerg_phone_num = emerg_phone_num
        
    def __str__(self):
        string = f"Patient's Name: {self.__fname} {self.__mname} {self.__lname}\n" \
         f"Patient's Address: {self.__address}\n" \
         f"Patient's City: {self.__city}, {self.__state}, {self.__zip}\n" \
         f"Patient's Phone number: {self.__phone_num}\n" \
         f"Patient's Emergency Contact: {self.__emerg_name}, {self.__emerg_phone_num}"

        
        return string
        
    
