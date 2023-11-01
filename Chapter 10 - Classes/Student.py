'''
Create a course class to help with creating course schedules
The course class should hvae the following private attributes
    * Course number
    * Couse name
    * Number of credit hours
Include public accessor and mutator methods for each of the private attributes
Include public initializer 
'''


class Student:

# Simple class for representing a course with number, name, and credit hours.

    def __init__(self, name = "", id_num = "", gpa = 0.0, courses = None):
        
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

        self.__name = name
        self.__id_num = id_num
        self.__gpa = gpa
        
        # Handle mutable default arguments of set()
        if courses is None:
            self.__courses = set()
        else:
            self.__courses = courses
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,n):
        self.__name = n
        
    @property
    def id_num(self):
        return self.__id_num
    @id_num.setter
    def id_num(self,id):
        self.__id_num = id
        
    @property
    def gpa(self):
        return self.__gpa
    @gpa.setter
    def gpa(self, gpa):
        self.__gpa = gpa
        
    @property
    def coures(self):
        return self.__courses
        
    
    def addCourse(self,course):
        ''' Add course to student schedule'''
        self.__courses.add(course)
        
    def withdrawCourse(self,course):
        self.__courses.discard()(course)
    
    def __str__(self):
        display_string = str('{:10} {:15}\n'.format('Name', self.__name) +
                             '{:10} {:15}\n'.format("ID", str(self.__id_num)) +
                             '{:10} {:<15.2f}\n'.format('GPA', (self.__gpa)) +
                             '{:10} {:15}\n'.format("Courses", str(self.__courses)))

        return display_string
    
if __name__ == "__main__":
    s1 = Student()
    print(s1)
    s2 = Student("Gabriel", "1634568", 3.92)
    print(s2)
    s3 = Student()
    s3.name = "Fiona Carruth"
    s3.id_num = "10234"
    s3.gpa = 4
    s3.addCourse("CIS1400")
    s3.addCourse("CIS2531")
    s3.addCourse("CIS2532")
    print(s3)