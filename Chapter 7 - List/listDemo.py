'''
'''

emptyList = [0,0,0,0]

emptyList2 = [0] * 5

evenNumbers = [2,4,6,8,10]

evenNumbers2 = list(range(2,11,2))

evenNumbers3 = [n * 2 for n in range (1,6)]

print("printing my empty list...",emptyList)
print("printing my empty list2...",emptyList2)
print("printing my even numbers...",evenNumbers)
print("printing my numbers2...",evenNumbers2)
print("printing my numbers3...",evenNumbers3)

# Acessing element through the index
index = 0
while index < 5:
    print(evenNumbers[index])
    index += 1
    
# Using for loop to access elements through the index
for i in range(len(evenNumbers)):
    print(evenNumbers[i])

for n in evenNumbers:
    print(emptyList2)


