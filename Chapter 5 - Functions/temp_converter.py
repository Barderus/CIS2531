'''
'''

def to_fahrenheit(temp):
    fahrenheit = (temp * 9/5) + 32
    print(temp, "Celsius in Fahrenheit is", format(fahrenheit, ".1f"), "degrees")

def to_celsius(temp):
    celsius = (temp - 32) / (9/5)
    print(temp, "Fahrenheit in Celsius is", format(celsius,".1f"), "degrees")

def main():
    while True:
        print()
        menu_choice = int(input("Enter: \n1 to convert to Celsius. \n2 to convert to Fahrenheit. \n0 to quit."))
        if menu_choice == 1:
            temp = float(input("Enter degrees in Fahrenheit: "))
            to_celsius(temp)
        elif menu_choice == 2:
            temp = float(input("Enter degrees in Celsius: "))
            to_fahrenheit(temp)
        elif menu_choice == 0:
            print("Exiting the program...")
            break
        else:
            print("Error!")
        
main()