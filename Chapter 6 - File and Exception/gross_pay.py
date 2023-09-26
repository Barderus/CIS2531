'''
This program calculates gross pay
'''

def main():
    
    while True:
        try:
            # Get the number of hours worked
            hours = int(input('Enter the hours worked this week: '))
            
            # Get the hourly pay rate
            pay_rate = float(input('Enter the hourly pay rate: '))
        except ValueError:
            print('ERROR: Hours worked and hourly pay rate must be valid numbers.')
        else:
            # Calculate the gross pay
            gross_pay = hours * pay_rate
            # Display the gross pay
            print('Gross pay: $', format(gross_pay, ',.2f'), sep='')
            break
        finally:
            print('This is the finally clause.')


# Call the main function
main()