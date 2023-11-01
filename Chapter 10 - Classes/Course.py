'''
Create a course class to help with creating course schedules
The course class should hvae the following private attributes
    * Course number
    * Couse name
    * Number of credit hours
Include public accessor and mutator methods for each of the private attributes
Include public initializer 
'''


class Course:

# Simple class for representing a course with number, name, and credit hours.

    def __init__(self, num = "", name = "", cr_hours = 0):
        
        '''
        The __init__ method initializes the student object characteristics
        as private data members.
        
        "courses" will be a non-duplicate set of course numbers
        
        Python GOTCHA
        Be careful with mutable default arguments:
        Python's default arguments are evaluated once when function
        is defined. Any mutation to default arguments will change object
        for future function calls
        '''

        self.__num = num
        self.__name = name
        self.__cr_hours = cr_hours
    
    # Mutator methods to set private attributes
    def setNum(self, num):
        self.__num = num
    def setName(self, name):
        self.__name = name
    def setCreditHours(self, cr_hours):
        self.__cr_hours
    
    # Accessor methods to get private attributes    
    def getNum(self):
        return self.__num
    def getName(self):
        return self.__name
    def getCreditHours(self):
        return self.__cr_hours

    def __str__(self):
        display_string = str('{}: {} ({} credit hours)\n'.format(self.__num,
                                                                self.__name,
                                                                self.__cr_hours))
        return display_string
    
if __name__ == "__main__":
    c1 = Course()
    print(c1)
    c2 = Course("CIS2531", "Intro to Python", 4)
    print(c2)
    c3 = Course()
    c3.setNum("CIS2532")
    c3.setName("Advanced Python")
    c3.setCreditHours(4)
    print(c3.getNum(), c3.getName(), c3.getCreditHours())
    print(c3)