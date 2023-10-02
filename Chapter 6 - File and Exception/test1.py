try:
    num = int(input('Enter an integer number to double: '))
except ValueError as err:
    print(err,'You entered an invalid value. Please enter a valid integer.')
else:
        print('The value doubled is', num * 2)
