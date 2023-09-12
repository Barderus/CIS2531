'''
Author: Gabriel dos Reis
Date: 9/12/2023
Program: loopManual
Description: Several little loop programs to practice loops
'''

# While loop
keep_going = "y"
while keep_going == "y":
    print("Hello Henry")
    print("Goodbye Henry")
    keep_going = "n"
    print("End of first while Loop")

# While loop with comparison
count = 10
while count >= 1:
    print("Hello number", count)
    count = count - 1
print("End of second While loop")

# Printing a list of numbers with For loop
for num in [1,2,3,4,5]:
    print(num)

# Printing a list of strings
for name in ["Gabriel", "Henry", "David"]:
    print(name) 

# Using range function with For loop
for num in range(5):                # for num in [0,1,2,3,4]
    print(num)                          #print(num)

# Using range to display a message x times
for x in range(2):
    print("I love guacamole!")
    
# Adding limit to the range
for num in range(12,15): 
    print(num) # Prints 12,13,14

#Adding a step value
for num in range(1,10,2): # Starting at 1, ends at 0, step 2 ()
    print(num)
    
# Using loop to add a series of numbers
total = 0 # Acumulator
max_numbers = (int(input("How many numbers would you like to add?: ")))
for counter in range(max_numbers):
    number = int(input("Enter a number:"))
    total += number # Or total = total + number
print("The total is", total)


#Sentinels
print("Beginning of Sentinel")
sentinel = 1
while sentinel != 0:
    sentinel = int(input("What's your favorite number? (Enter 0 to stop)"))
    
#Input validation
score = int(input("Enter test score:"))
while score < 0 or score > 100:
    print("Error! The score cannot be negative or more than 100!")
    score = int(input("Enter the correct score: "))
    
# Nested Loop
BASE_SIZE = 8
for row in range(BASE_SIZE):
    for collum in range (row+1):
        print("*", end="")
    print()