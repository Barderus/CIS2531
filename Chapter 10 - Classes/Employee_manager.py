'''
Create a program that stores Employee objects in a dictionary. 
Use the employee ID number as the key. The program should present a menu that lets the user perform the following actions:
  •	Look up an employee in the dictionary 
  •	Add a new employee to the dictionary 
  • Change an existing employee’s name, department, and job title in the dictionary 
  •	Delete an employee from the dictionary 
  •	Quit the program 
When the program ends, it should pickle the dictionary and save it to a file. 
Each time the program starts, it should try to load the pickled dictionary from the file. 

'''
'''
    * Name
    * ID number
    * Department
    * Job title
    '''
import Employee as emp 
def main():
    employee1 = emp("Gabriel", "12345", "Applied Science", "Data Analyst")
    print(employee1, "\n")
    employee2 = emp("Fiona", "67890", "Biology", "Veterinary")
    print(employee2, "\n")
    employee3 = emp("Henry", "10293", "Kidspalooza", "Child")
    print(employee3)

main()