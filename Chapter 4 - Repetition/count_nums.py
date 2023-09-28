'''
Count the total numbers of digits in a number using while loop
'''

num = int(input("Enter number: "))
counter = 0
while num != 0:
    num = num // 10
    counter += 1
print("The number you entered has", counter, "digits.")