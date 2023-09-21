import calculator as calc

def main():
    display_menu()
    
    sentinel = False
    while sentinel != True:
        user_choice = int(input("Enter your calculation choice: (-1 to exit) "))
        
        if user_choice == 1:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = calc.addition(num1,num2)
            print("The sum of", num1, "and", num2, "is", format(result,".1f"))
        elif user_choice == 2:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = calc.subtraction(num1,num2)
            print("The subtraction of", num1, "and", num2, "is", format(result,".1f"))
        elif user_choice == 3:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = calc.multiplication(num1,num2)
            print("The multiplication of", num1, "and", num2, "is", format(result,".1f"))
        elif user_choice == 4:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = calc.division(num1,num2)
            print("The division of", num1, "and", num2, "is", format(result,".1f"))
        elif user_choice == -1:
            sentinel = True
            print("Exiting the program...")

def display_menu():
    print("Calculator Menu")
    print("---------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication") 
    print("4. Division")
    #print("5. Percentage")
    print("5. Quit")   
    print()

main() 