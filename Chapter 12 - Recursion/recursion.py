'''
Use recursive functions to find: Fibonnaci sequence, factorial, greatest common divisor,
least divisor.
'''

# Function to find the nth number in the Fibonnaci sequence
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
     
# Function to find the factorial of a number
def factorial(num):
    # Base case
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
# Function to find the greatest common divisor of two numbers
def greastest(num1, num2):
    # Base case
    if num2 == 0:
        return num1
    else:
        return greastest(num2, num1 % num2)
    
# Function to find the least common divisor of two numbers
def least(num1, num2):
    # Base case
    if num1 == 0:
        return num2
    else:
        return least(num2 % num1, num1)
    
def menu():
    print("1. Display Fibonacci Sequence")
    print("2. Calcualtes the factorial of a number")
    print("3. Calculate  the greatest common divisor of two numbers")
    print("4. Calculate the least common divisor of two numbers")
    print("5. Exit")
    print()
    
def main():
    
    while True:
        menu()
        menu_choice = int(input("Enter your menu option: "))
        if menu_choice == 5:
            break
        if menu_choice == 1:
            nth_number = int(input("Enter how many numbers would you like to see from the sequence: "))
            print("Fibonacci Sequence:", end=" ")
            for i in range(nth_number):
                print(fibonacci(i), end=" ")
            print()
        elif menu_choice == 2:
            factorial_number = int(input("Enter the factorial number: "))
            print("The factorial of", factorial_number, "is", factorial(factorial_number))
            print()
        elif menu_choice == 3:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print("The GFC between", num1, "and", num2, "is:", greastest(num1, num2))
            print()
        elif menu_choice == 4:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print("The LCD between", num1, "and", num2, "is:", least(num1, num2))
        else:
            print("Error! Invalid input. Try again.")
            
# Call main and starts the program    
main()