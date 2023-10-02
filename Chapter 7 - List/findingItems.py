'''
Finding item in lists
item in listName
'''

oddNumbers = [1,3,5,7,9,11]

# Checking if 5 is in the list
print("Is 5 in the oddNumbers list?")
print(5 in oddNumbers)


# Checking if 10 is in the list
print("Is 10 in the oddNumber list?")
print(10 in oddNumbers)

# Check if not in the list
print("Is three not in the list?")
print("three" not in oddNumbers)

# Count method - 0 = false, 1 = true
print("Count method...")
print(oddNumbers.count(10))
print(oddNumbers.count(3))