'''
Processing list
'''
import random

evenNumbers = [2,6,10,22, 30, 98, 14, 4]

# Finding total
total = 0
for value in evenNumbers:
    total += value
    
print("Total: ", total)

# Calculate average
avg = total / len(evenNumbers)
print("Average: ", avg)

# Get random number from the list
print(random.choice(evenNumbers))

# Get random from the list using choices
print(random.choices(evenNumbers, k = 3))

# Write a list to the files
# Writelines do not allow you to add spaces. So it's better to use loop and write() function

