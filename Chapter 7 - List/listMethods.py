'''
Built-in methods
'''


listNumbers = [1, 0, 100, 101, 1001, 1110, 10101, 1010]
evenNumbers = [2,6,10,22, 30, 98, 14, 4]

# Append
listNumbers.append(1001001)
# Print the index of the 2nd item
print(listNumbers.index(100))

# Determine wheter item is contained in sequence
#print(listNumbers.index(1001001,2,4))


# Reverse list
evenNumbers.reverse()
print(evenNumbers)

# Sort list
evenNumbers.sort()
print(evenNumbers)

# Delete item of that index
del evenNumbers[4]
print(evenNumbers)

# Min/Max method
print("Min number:", min(evenNumbers))
print("Max number: ", max(evenNumbers))

# Copy method/ shallow copy
evenNumCopy = evenNumbers.copy()
print("EvenNumbers copy: ", evenNumCopy)

# Loop to append each element to a list
eNums = [10,20,30]
for item in evenNumbers:
    eNums.append(item)
    
print(eNums)   
eNums.clear()

# Concatenation or extend for empty list only
eNums = [] + listNumbers
print(eNums)
eNums.clear()

eNums = [n for n in evenNumbers]
print(eNums)

# Calc average of a list