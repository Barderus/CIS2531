'''
Calculate the sum of all numbers from 1 to a given number
'''

max_number = int(input("Enter the max number: "))
accumaltor = 0
for n in range(1, max_number+1):
    accumaltor += n
print(accumaltor)
    