'''
Author: Gabriel dos Reis
Program: BankManager.py
Description:
    This program allows the user to manage his bank account using a menu interface. 
    It also stores every transaction into a file.

'''
from datetime import date
from Bank import Checkings 
from Bank import Savings 
from Bank import Transactions
from Bank import Customer
import pickle

# This function writes down every transaction made by the user into a file
def store_transaction():
    
    '''
        This function stores the transaction on a file with the following
        parameter: {date : information}
    '''
    
    pass

def store_acc():
    '''
        This function store all the accounts into a dictionary such {account number : [all the bank information]}
    '''
    pass

# This function displays the transaction history of an specific account
def show_history():
    '''
        This function allows the user to look up for a transaction
        in a certain day
    '''
    pass

def main_menu():
    
    '''
        This function is used to display the main menu so the user can interact with the application
    '''
    
    print("\t**** MAIN MENU ****")
    print("1. Deposit money into an account\
          \n2. Withdraw money from the account.\
          \n3. See Balance\
          \n4. Transfer money to another account.\
          \n5. Look up history\
          \n0. Quit")
    choice = int(input("Enter the operation code: "))
    return choice

def create_checkings():
    acc_type = "Checking Account"
    name = input("Enter your name: ")
    acc_num = input("Enter your account number: ")
    exp_date = input("Enter the expire date: ")
    cv = input("Enter the security code: ")
    
    checkings = Checkings(name, acc_num, exp_date, cv, acc_type, 0.0)
    return checkings
    
def create_savings():
    acc_type = "Savings Account"
    name = input("Enter your name: ")
    acc_num = input("Enter your account number: ")
    exp_date = input("Enter the expire date: ")
    cv = input("Enter the security code: ")
    interest_rate = float(input("Enter the interest rate on this account: "))
    
    savings = Savings(name, acc_num, exp_date, cv, acc_type, 0.0, interest_rate)
    return savings

def create_account():
        while True:
            print("I see you do not have an account with us yet. To use our bank operations you need to have an account.")
            acc_type = input("Enter bank account type you would like to create (Checkings / Savings): ")
            if acc_type == "checkings":
                checkings = create_checkings()

            elif acc_type == "savings":
                savings = create_savings()
            else:
                print("Invalid entry. Choose between checkings or savings.")

            sentinel = input("\nWould you like to enter another account? (y/n): ")
            if sentinel.lower() == "y":
                print()
                continue
            else:
                print()
                break

def see_balance(checkings, savings):
    
    '''
        This function allows the user to see their balance
        in either the checkings or savings account
    '''
    
    choice = input("Would you like to see your balance on which account? (checkings/savings): ")
    if choice == "checkings":
        print(f"\tBalance Available: {checkings.get_balance()}\n")
    elif choice == "savings":
        print(f"\tBalance Available: {savings.get_balance()}\n")
        
def deposit_money(checkings, savings):
        
    ''' 
        This function allows the user to deposit money in either
        checkings or savings account.
        It takes as arguments the object checkings and savings.
    '''
        
    print("Deposit money\n")
    choice = input("Would like to deposit money from which account? (Checkings / Savings)?: ")
    if choice == "checkings":
        deposit_amnt = float(input("How much would like to depoit?: "))
        checkings.deposit(deposit_amnt)
        today = date.today()
        day = today.strftime("%m/%d/%y")

        print("Today's date", day)
        print(f"${deposit_amnt} was deposited in your checkings account.")

    elif choice == "savings":
        deposit_amnt = float(input("How much would like to depoit?: "))
        savings.deposit(deposit_amnt)
        print(f"${deposit_amnt} was deposited in your savings account.")
        
def withdraw_money(checkings, savings):
    
    '''
        This function allows the usert to withdraw money from
        either checkings or savings account.
    '''
    
    print("Withdraw Money\n")
    choice = input("Would like to withdraw money from which account? (Checkings / Savings)?: ")
    if choice == "checkings":
        deposit_amnt = float(input("How much would like to withdraw?: "))
        checkings.withdraw(deposit_amnt)
        print(f"${deposit_amnt} was withdrawn in your checkings account.")
    elif choice == "savings":
        deposit_amnt = float(input("How much would like to withdraw?: "))
        savings.withdraw(deposit_amnt)
        print(f"${deposit_amnt} was withdrawn in your savings account.")
    print(f"\n\tYou have {checkings.get_balance()} in your balance")

def transfer_money(checkings, savings):
    
    '''
        This function allows the user to transer money
        between two accounts.
    '''
    
    print("Transfer Money\n")
    from_acc = input("What account are you transfering from?: ")
    to_acc = input("What account are you transfering to?: ")
    if to_acc == "checkings" and from_acc == "savings":
        print(f"You have {checkings.get_balance()} availabe in your {to_acc} account.")
        amnt = float(input("How much would you like to transfer?: "))
        checkings.transfer(savings, amnt)
        print("Transfer completed with sucess.")
    elif to_acc == "savings" and from_acc == "checkings":
        print(f"You have {savings.get_balance()} availabe in your {to_acc} account.")
        amnt = float(input("How much would you like to transfer?: "))
        savings.transfer(checkings, amnt)
        print("Transfer completed with sucess.")
   
# Main function
def main():
    
    checkings = None
    savings = None
    # Dictionary to add customer account
    acc_dic = {}

    print("\t WELCOME TO THE BANK OF THE TOILET ")
    acc_num = input("Enter bank account number: ")
    
    if acc_num in acc_dic:
        print("Hello", dic.userName)
        main_menu()
    else:
        create_account()
    '''
        If the acc_num prompt exist in the dictionary:
            print("Hello user")
            then display the user the main menu and operations
        But if acc_num does not exist, then it prompts user to open an account
            then display the main menu and operations.
        
    '''    
    
    while True:
        operation = main_menu()
        
        if operation == 1:
            deposit_money(checkings, savings)
        elif operation == 2:
            withdraw_money(checkings, savings)
        elif operation == 3:
            see_balance(checkings, savings)
        elif operation == 4:
            transfer_money(checkings, savings)
        elif operation == 5:
            show_history(checkings, savings)
        elif operation == 0:
            quit()
            
# Call main
if __name__ == "__main__":
    main()
    