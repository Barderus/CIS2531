'''
Author: Gabriel dos Reis
Date: 11/14/2023
Program: Employee_demo.py
Description:
Prompt and display:
    Employee's name
    Employee's number
    Employee's shift number
    Employee's hourly pay rate
    Yearly gross pay
'''
from Employee import ProductionWorker as Worker
from Employee import ShiftSupervisor as Supervisor
def employee_entry():
    name = input("Enter employee's name: ")
    number = input("Enter employee's number: ")
    shift_number = int(input("Enter employee's shift number (1 for day, 2 for night): "))
    pay_rate = float(input("Enter Employee's hourly pay rate: "))
    
    worker1 = Worker(name.title(), number, shift_number, pay_rate )

    print()
    print("*** EMPLOYEE *** ")
    print(f"Employee Name: {worker1.name}")
    print(f"Employee Number: {worker1.number}")
    print(f"Shift number: {worker1.determineShift()}")
    print(f"Hourly pay rate: ${worker1.pay_rate:,.2f}")
    print(f"Yearly Gross pay: ${worker1.gross_pay():,.2f}")
    print()
    
def supervisor_entry():
    name = input("Enter supervisor's name: ")
    number = input("Enter supervisor's number: ")
    salary = float(input("Enter supervisor's salary: "))
    bonus = float(input("Enter supervisor's bonus: "))
    
    supervisor = Supervisor(name.title(), number, salary, bonus)
    
    print()
    print("*** SUPERVISOR *** ")
    print(f"Supervisor Name: {supervisor.name}")
    print(f"Supervisor Number: {supervisor.number}")
    print(f"Yearly Gross pay: ${supervisor.gross_pay():,.2f}")
    print()

def main():
    
    while True:
        print("Would you like to enter data for: \n\t1. Employee\n\t2. Supervisor\n\t3. Quit")
        choice = int(input("Enter your selection (1/2/3): "))
        
        if choice == 1:
            employee_entry()
        elif choice == 2:
            supervisor_entry()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        more_data = input("Would you like to enter more data? (y/n): ")
        if more_data.lower() != 'y':
            break
 
main()

'''
Would you like to enter data for: 
        1. Employee
        2. Supervisor
        3. Quit
Enter your selection (1/2/3): 1
Enter employee's name: bob williams
Enter employee's number: 111
Enter employee's shift number (1 for day, 2 for night): 1
Enter Employee's hourly pay rate: 18.75

*** EMPLOYEE ***
Employee Name: Bob Williams
Employee Number: 111
Shift number: Day shift (1)
Hourly pay rate: $18.75
Yearly Gross pay: $39,000.00

Would you like to enter more data? (y/n): y     
Would you like to enter data for:
        1. Employee
        2. Supervisor
        3. Quit
Enter your selection (1/2/3): 1
Enter employee's name: Sue Johnson
Enter employee's number: 222
Enter employee's shift number (1 for day, 2 for night): 2
Enter Employee's hourly pay rate: 22.75

*** EMPLOYEE ***
Employee Name: Sue Johnson
Employee Number: 222
Shift number: Night shift (2)
Hourly pay rate: $22.75
Yearly Gross pay: $47,320.00

Would you like to enter more data? (y/n): y     
Would you like to enter data for:
        1. Employee
        2. Supervisor
        3. Quit
Enter your selection (1/2/3): 2
Enter supervisor's name: dawshannell bridges
Enter supervisor's number: 333
Enter supervisor's salary: 55000.00
Enter supervisor's bonus: 1500.00

*** SUPERVISOR ***
Supervisor Name: Dawshannell Bridges
Supervisor Number: 333
Yearly Gross pay: $56,500.00

Would you like to enter more data? (y/n): n
'''