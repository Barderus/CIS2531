'''
Author: Gabriel dos Reis
Date: 11/1/2023
Program: Employee. py
Description:
Write a class named Employee that holds the following data about an employee in attributes: 
    * Name
    * ID number
    * Department
    * Job title
Once you have written the class, write a program that creates three Employee objects to hold the following data:
The program should store this data in the three objects, then display the data for each employee on the screen
'''

class Employee():
    def __init__(self, name, id_num, deptment, job_title):
        self.__name = name
        self.__id_num = id_num
        self.__deptment = deptment
        self.__job_title = job_title
        
    
    # Setter
    def set_name(self, name):
        self.__name = name
        
    def set_id_num(self, id_num):
        self.__id_num = id_num
    
    def set_deptment(self, deptment):
        self.__deptment = deptment
        
    def set_job_title(self, job_title):
        self.__job_title = job_title
    
    # Getter
    def get_name(self):
        return self.__name
    
    def get_id_num(self):
        return self.__id_num
    
    def get_deptment(self):
        return self.__deptment
    
    def get_job_title(self):
        return self.__job_title
    
    def __str__(self):
        
        employee = f"Employee name: {self.__name}\tEmplyee's ID number: {self.__id_num}\nEmployee's Department: {self.__deptment}\tEmployee's Job Title: {self.__job_title}"
        
        return employee
    
if __name__ == "__main__":
    employee1 = Employee("Gabriel", "12345", "Applied Science", "Data Analyst")
    print(employee1, "\n")
    employee2 = Employee("Fiona", "67890", "Biology", "Veterinary")
    print(employee2, "\n")
    employee3 = Employee("Henry", "10293", "Kidspalooza", "Child")
    print(employee3)
    
