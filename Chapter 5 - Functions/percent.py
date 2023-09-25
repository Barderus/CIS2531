'''
Calculates the percentage
'''

def get_percent(num1, num2):
    
    ratio = num1 / num2
    percent = ratio * 100
    return percent
    
    
    
def main():
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter the second number: "))
    print(get_percent(num1, num2), "%")

main()