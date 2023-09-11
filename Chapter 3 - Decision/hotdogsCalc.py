'''
Author: Gabriel dos Reis
Date: 9/6/2023
Program: hotDogCalc.py
Description: Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. 
Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns
needed for a cookout, with the minimum amount of leftovers. 
The program should ask the user for the number of people attending the cookout and the number of hot dogs 
each person will be given. The program should display the following details:
        The minimum number of packages of hot dogs required
                
        The minimum number of packages of hot dog buns required
                
        The number of hot dogs that will be left over
                
        The number of hot dog buns that will be left over
'''
# named constants
HOT_DOGS_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# Prompt user for the number of people coming and how many hot dogs they are eating
numPeople = int(input("How many people will be attending the cookout?: "))
hotDogsPerPerson = int(input("How many hot dogs will be given to each atendee?: "))

#Find the total amount of Hot dogs to be made
ttlHotDogs = numPeople * hotDogsPerPerson
# Find how many packages of hot dogs are needed 
packgeHotDogs = ttlHotDogs // HOT_DOGS_PACKAGE
# Find how many packages of hot dogs are needed 
packageBuns = ttlHotDogs / BUNS_PER_PACKAGE
# Find how many buns left overs are there, if any
leftOvers =  (round(packageBuns) * BUNS_PER_PACKAGE) - ttlHotDogs

# Display the result
print("Total amount of hot dogs:", ttlHotDogs)
print("Amount of hot dogs packages to buy:", packgeHotDogs)
print("Amount of bun packages to buy: ", round(packageBuns))
print("Leftovers buns:", leftOvers)

# Output sample:
'''
How many people will be attending the cookout?: 30
How many hot dogs will be given to each atendee?: 5
Total amount of hot dogs: 150
Amount of hot dogs packages to buy: 15
Amount of bun packages to buy:  19
Leftovers buns: 2
'''

