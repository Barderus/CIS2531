'''
Maximum of Two Values
'''

def check_highest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
def main():
    num1 = int(input(" Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    highest_num = check_highest(num1, num2)
    print("The highest number between", num1, "and", num2, "is",highest_num )
    
main()